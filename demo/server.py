"""Chạy bằng python demo/server.py, phục vụ demo tại loopback."""
import argparse
import csv
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "codebase"))
import agent
import tracing
sys.path.insert(0, str(ROOT / "eval"))
from grade_helper import evaluate_row


def history():
    runs = []
    for p in sorted((ROOT / "eval").glob("run-*.csv"), key=lambda f: int(f.stem[4:]) if f.stem[4:].isdigit() else 0):
        if not p.stem[4:].isdigit():
            continue
        with p.open(encoding="utf-8-sig", newline="") as f:
            rows = list(csv.DictReader(f))
        for row in rows:
            row["auto"] = evaluate_row(row["id"], row["output"])["code_ok"]
        if rows:
            runs.append({"name":p.stem, "id":rows[0]["run_id"], "cases":rows})
    return runs


class Handler(BaseHTTPRequestHandler):
    def reply(self, code, content, mime):
        self.send_response(code)
        self.send_header("Content-Type", mime)
        self.send_header("Content-Length", str(len(content)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(content)

    def data(self, code, payload):
        self.reply(code, json.dumps(payload, ensure_ascii=False).encode(), "application/json; charset=utf-8")

    def do_GET(self):
        if self.path == "/api/runs":
            return self.data(200, history())
        if self.path in ("/", "/index.html"):
            return self.reply(200, (Path(__file__).parent / "index.html").read_bytes(), "text/html; charset=utf-8")
        self.send_error(404)

    def do_POST(self):
        if self.path != "/api/plan":
            return self.send_error(404)
        port = self.server.server_port
        origins = {f"http://{host}:{port}" for host in ("localhost","127.0.0.1")}
        if self.headers.get("Origin") not in origins or self.headers.get_content_type() != "application/json":
            return self.data(403, {"error":"Hãy mở demo tại địa chỉ cục bộ."})
        try:
            size = int(self.headers.get("Content-Length", 0))
            if not 0 < size <= 16000:
                raise ValueError()
            q = json.loads(self.rfile.read(size))["text"]
            if not isinstance(q,str) or not 0 < len(q.strip()) <= 3000:
                raise ValueError()
        except (ValueError, KeyError, TypeError):
            return self.data(400, {"error":"Nhập yêu cầu từ 1 đến 3.000 ký tự."})
        tracing.begin("demo")
        try:
            result = agent.answer(q)
        except Exception:
            return self.data(502, {"error":"Không tạo được lịch. Kiểm tra kết nối và cấu hình model trên máy demo."})
        finally:
            stats, _ = tracing.end()
        self.data(200, {"output":result["output"], "stats":stats})


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--snapshot", action="store_true")
    args = parser.parse_args()
    if args.snapshot:
        html = (Path(__file__).parent / "index.html").read_text("utf8")
        payload = json.dumps(history(), ensure_ascii=False).replace("<", "\\u003c")
        (ROOT / "demo.html").write_text(html.replace("/* SAVED_RUNS */", "window.savedRuns = " + payload + ";"), encoding="utf8")
    else:
        server = HTTPServer(("127.0.0.1", args.port), Handler)
        print(f"Demo ApexFour: http://127.0.0.1:{server.server_port}/",flush=True)
        server.serve_forever()

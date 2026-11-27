"""Nối model — chỗ DUY NHẤT trong bản chạy thử gọi model AI. Nhóm ApexFour (Track C · C1).

Hợp đồng (giữ nguyên để khung đo được token):
    call_model(system: str, user: str) -> dict với 4 khoá
        "text":       str   chữ model trả về
        "model":      str   tên model đã gọi (để tra giá ở bảng giá model)
        "tokens_in":  int   số token vào, lấy từ trường usage trong phản hồi API — KHÔNG ước lượng
        "tokens_out": int   số token ra, gồm cả token suy luận / suy nghĩ nếu API tính riêng
    @model_call (từ tracing.py) tự ghi mỗi lần gọi vào trace; agent.py gọi call_model bao nhiêu lần
    cũng được, khung tự cộng token.
    Lỗi gọi model (hết lượt, sai key, mất mạng): cứ để exception bay ra — khung ghi lỗi vào cột error.

Hỗ trợ trực tiếp bằng thư viện chuẩn Python (urllib, không cần pip install):
    - fake       : chế độ giả khi chưa điền .env (token = 0, không tính lượt eval/simulate)
    - gemini     : Google Gemini API (generativelanguage.googleapis.com)
    - openai     : OpenAI Chat Completions (và các nhà cung cấp tương thích qua API_BASE_URL)
    - groq       : Groq OpenAI-compatible API
    - deepseek   : DeepSeek OpenAI-compatible API
    - openrouter : OpenRouter OpenAI-compatible API
    - anthropic  : Anthropic Messages API (Claude)
    - ollama     : Model chạy cục bộ qua http://localhost:11434/api/chat

Không dán API key vào file này. Điền MODEL_PROVIDER, MODEL_NAME, API_KEY vào .env (không commit).
"""
import json
import os
import urllib.error
import urllib.parse
import urllib.request

from tracing import model_call

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_env(path=os.path.join(ROOT, ".env")):
    """Đọc file .env (KEY=VALUE mỗi dòng) vào biến môi trường, không ghi đè biến đã có. Khung — không cần sửa."""
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8-sig") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


load_env()
MODEL_PROVIDER = (os.environ.get("MODEL_PROVIDER") or "fake").strip().lower()
MODEL_NAME = (os.environ.get("MODEL_NAME") or "").strip()
API_KEY = (os.environ.get("API_KEY") or "").strip()
API_BASE_URL = (os.environ.get("API_BASE_URL") or "").strip()
SHOW_RAW = (os.environ.get("SHOW_RAW") or "").strip().lower() in ("1", "true", "yes")

OPENAI_COMPAT_URLS = {
    "openai": "https://api.openai.com/v1/chat/completions",
    "groq": "https://api.groq.com/openai/v1/chat/completions",
    "deepseek": "https://api.deepseek.com/chat/completions",
    "openrouter": "https://openrouter.ai/api/v1/chat/completions",
}
URL_CLAUDE = "https://api.anthropic.com/v1/messages"
URL_OLLAMA = "http://localhost:11434/api/chat"
URL_GEMINI_TMPL = "https://generativelanguage.googleapis.com/v1beta/models/%s:generateContent"


def post_json(url, headers, body, timeout=90):
    """Gửi POST JSON bằng thư viện chuẩn (urllib), trả về dict JSON phản hồi."""
    req = urllib.request.Request(
        url,
        data=json.dumps(body, ensure_ascii=False).encode("utf-8"),
        method="POST",
        headers=dict({"Content-Type": "application/json"}, **headers),
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")[:400]
        raise RuntimeError("HTTP %d từ %s: %s" % (e.code, url.split("?")[0], detail))
    if SHOW_RAW:
        print(json.dumps(data, ensure_ascii=False, indent=2)[:3000])
    return data


def _require_config(need_key=True):
    if not MODEL_NAME:
        raise RuntimeError(
            "Thiếu MODEL_NAME trong .env (ví dụ: gemini-3.1-flash-lite hoặc gemini-2.5-flash). Xem docs/connect-model.md"
        )
    if need_key and not API_KEY:
        raise RuntimeError(
            "Thiếu API_KEY trong .env cho MODEL_PROVIDER=%s. Sao chép .env.example thành .env và điền key."
            % MODEL_PROVIDER
        )


def call_gemini(system: str, user: str) -> dict:
    """Gọi Google Gemini REST API (generateContent), lấy token thật từ usageMetadata."""
    _require_config(need_key=True)
    model_path = urllib.parse.quote(MODEL_NAME, safe="-._")
    url = API_BASE_URL or (URL_GEMINI_TMPL % model_path)
    body = {
        "contents": [{"role": "user", "parts": [{"text": user}]}],
        "generationConfig": {"temperature": 0.2},
    }
    if system:
        body["systemInstruction"] = {"parts": [{"text": system}]}
    data = post_json(url, {"x-goog-api-key": API_KEY}, body)

    candidates = data.get("candidates") or []
    if not candidates:
        block = data.get("promptFeedback") or {}
        raise RuntimeError("Gemini không trả về candidates (promptFeedback=%r)" % (block,))
    parts = (candidates[0].get("content") or {}).get("parts") or []
    # Bỏ các phần suy nghĩ nội bộ (thought=True) nếu model có thinking mode
    text = "".join(p.get("text", "") for p in parts if not p.get("thought"))
    if not text:
        text = "".join(p.get("text", "") for p in parts)

    usage = data.get("usageMetadata") or {}
    if "promptTokenCount" not in usage:
        raise RuntimeError("Phản hồi Gemini thiếu usageMetadata.promptTokenCount (bật SHOW_RAW=1 để kiểm tra)")
    tokens_in = int(usage["promptTokenCount"])
    if "candidatesTokenCount" in usage or "thoughtsTokenCount" in usage:
        tokens_out = int(usage.get("candidatesTokenCount") or 0) + int(usage.get("thoughtsTokenCount") or 0)
    elif "totalTokenCount" in usage:
        tokens_out = max(0, int(usage["totalTokenCount"]) - tokens_in)
    else:
        raise RuntimeError("Phản hồi Gemini thiếu số token đầu ra trong usageMetadata")
    return {"text": text, "tokens_in": tokens_in, "tokens_out": tokens_out}


def call_openai_compat(system: str, user: str, default_url: str) -> dict:
    """Gọi OpenAI hoặc nhà cung cấp tương thích Chat Completions (Groq, DeepSeek, OpenRouter)."""
    _require_config(need_key=True)
    url = API_BASE_URL or default_url
    messages = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": user}]
    headers = {"Authorization": "Bearer " + API_KEY}
    # Không truyền temperature mặc định để tương thích các model reasoning/nano mới của OpenAI (vd gpt-5.4-nano)
    body = {"model": MODEL_NAME, "messages": messages}
    data = post_json(url, headers, body)
    usage = data.get("usage") or {}
    if "prompt_tokens" not in usage or "completion_tokens" not in usage:
        raise RuntimeError("Phản hồi API thiếu trường usage.prompt_tokens / completion_tokens")
    text = data["choices"][0]["message"]["content"] or ""
    return {
        "text": text,
        "tokens_in": int(usage["prompt_tokens"]),
        "tokens_out": int(usage["completion_tokens"]),
    }


def call_claude(system: str, user: str) -> dict:
    """Gọi Anthropic Claude Messages API, lấy token thật từ usage."""
    _require_config(need_key=True)
    url = API_BASE_URL or URL_CLAUDE
    data = post_json(
        url,
        {"x-api-key": API_KEY, "anthropic-version": "2023-06-01"},
        {
            "model": MODEL_NAME,
            "max_tokens": 2048,
            "temperature": 0.2,
            "system": system or "",
            "messages": [{"role": "user", "content": user}],
        },
    )
    text = "".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text")
    usage = data.get("usage") or {}
    return {"text": text, "tokens_in": int(usage["input_tokens"]), "tokens_out": int(usage["output_tokens"])}


def call_ollama(system: str, user: str) -> dict:
    """Gọi model cục bộ qua Ollama."""
    _require_config(need_key=False)
    url = API_BASE_URL or URL_OLLAMA
    messages = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": user}]
    data = post_json(url, {}, {"model": MODEL_NAME, "messages": messages, "stream": False}, timeout=300)
    return {
        "text": data["message"]["content"],
        "tokens_in": int(data.get("prompt_eval_count") or 0),
        "tokens_out": int(data.get("eval_count") or 0),
    }


@model_call
def call_model(system: str, user: str) -> dict:
    if MODEL_PROVIDER == "fake":
        last = (user.strip().splitlines() or [""])[-1]
        return {"text": "[câu trả lời giả — chưa nối model] " + last[:60], "model": "fake", "tokens_in": 0, "tokens_out": 0}

    if MODEL_PROVIDER == "gemini":
        r = call_gemini(system, user)
    elif MODEL_PROVIDER in OPENAI_COMPAT_URLS:
        r = call_openai_compat(system, user, OPENAI_COMPAT_URLS[MODEL_PROVIDER])
    elif MODEL_PROVIDER == "anthropic":
        r = call_claude(system, user)
    elif MODEL_PROVIDER == "ollama":
        r = call_ollama(system, user)
    else:
        raise NotImplementedError(
            "Không hỗ trợ MODEL_PROVIDER=%s (hỗ trợ: gemini, openai, groq, deepseek, openrouter, anthropic, ollama, fake)."
            % MODEL_PROVIDER
        )
    return {
        "text": r["text"],
        "model": MODEL_NAME,
        "tokens_in": int(r["tokens_in"]),
        "tokens_out": int(r["tokens_out"]),
    }

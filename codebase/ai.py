"""Nối model — chỗ DUY NHẤT trong bản chạy thử gọi model AI.

Hợp đồng (giữ nguyên để khung đo được token):
    call_model(system: str, user: str) -> dict với 4 khoá
        "text":       str   chữ model trả về
        "model":      str   tên model đã gọi (để tra giá ở bảng giá model)
        "tokens_in":  int   số token vào, lấy từ trường usage trong phản hồi API — KHÔNG ước lượng
        "tokens_out": int   số token ra, gồm cả token suy luận / suy nghĩ nếu API tính riêng
    @model_call (từ tracing.py) tự ghi mỗi lần gọi vào trace; agent.py gọi call_model bao nhiêu lần
    cũng được, khung tự cộng token.
    Lỗi gọi model (hết lượt, sai key, mất mạng): cứ để exception bay ra — khung ghi lỗi vào cột error.

Hỗ trợ qua .env (chỉ dùng thư viện chuẩn urllib):
    MODEL_PROVIDER = fake | gemini | openai | groq | openrouter | deepseek | anthropic | ollama
"""
import json
import os
import urllib.error
import urllib.parse
import urllib.request

from tracing import model_call

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHOW_RAW = False


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

OPENAI_COMPAT_URLS = {
    "openai": "https://api.openai.com/v1/chat/completions",
    "groq": "https://api.groq.com/openai/v1/chat/completions",
    "openrouter": "https://openrouter.ai/api/v1/chat/completions",
    "deepseek": "https://api.deepseek.com/chat/completions",
}
URL_CLAUDE = "https://api.anthropic.com/v1/messages"
URL_OLLAMA = "http://localhost:11434/api/chat"


def post_json(url: str, headers: dict, body: dict, timeout: int = 90) -> dict:
    """Gửi POST JSON, trả về JSON phản hồi. Chỉ dùng thư viện chuẩn (urllib)."""
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        method="POST",
        headers=dict({"Content-Type": "application/json", "User-Agent": "ApexFour-TrackC/1.0"}, **headers),
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")[:400]
        raise RuntimeError("HTTP %d: %s" % (e.code, detail))
    if SHOW_RAW:
        print(json.dumps(data, ensure_ascii=False, indent=2)[:3000])
    return data


def _require_credentials(need_key: bool = True) -> None:
    if not MODEL_NAME:
        raise RuntimeError("Thiếu MODEL_NAME trong .env (xem .env.example và docs/connect-model.md).")
    if need_key and not API_KEY:
        raise RuntimeError("Thiếu API_KEY trong .env cho MODEL_PROVIDER=%s." % MODEL_PROVIDER)


def call_gemini(system: str, user: str) -> dict:
    """Google AI Studio (Gemini generateContent REST API)."""
    _require_credentials(need_key=True)
    model_id = MODEL_NAME[7:] if MODEL_NAME.startswith("models/") else MODEL_NAME
    base = API_BASE_URL or "https://generativelanguage.googleapis.com/v1beta"
    url = "%s/models/%s:generateContent?key=%s" % (
        base.rstrip("/"),
        urllib.parse.quote(model_id, safe="-._"),
        urllib.parse.quote(API_KEY, safe=""),
    )
    body = {
        "contents": [{"role": "user", "parts": [{"text": user}]}],
        "generationConfig": {"temperature": 0.2},
    }
    if system:
        body["systemInstruction"] = {"parts": [{"text": system}]}
    data = post_json(url, {}, body)
    candidates = data.get("candidates") or []
    parts = (candidates[0].get("content") or {}).get("parts") or [] if candidates else []
    text = "".join(p.get("text", "") for p in parts if not p.get("thought"))
    usage = data.get("usageMetadata") or {}
    tokens_in = int(usage.get("promptTokenCount") or 0)
    tokens_out = int(usage.get("candidatesTokenCount") or 0) + int(usage.get("thoughtsTokenCount") or 0)
    return {"text": text, "tokens_in": tokens_in, "tokens_out": tokens_out}


def call_openai_compat(system: str, user: str, default_url: str) -> dict:
    """OpenAI và các nhà cung cấp tương thích OpenAI (Groq, OpenRouter, DeepSeek…)."""
    _require_credentials(need_key=True)
    url = API_BASE_URL or default_url
    messages = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": user}]
    data = post_json(
        url,
        {"Authorization": "Bearer " + API_KEY},
        {"model": MODEL_NAME, "messages": messages},
    )
    usage = data.get("usage") or {}
    msg = ((data.get("choices") or [{}])[0].get("message") or {})
    content = msg.get("content") or ""
    if isinstance(content, list):
        content = "".join(part.get("text", "") for part in content if isinstance(part, dict))
    tokens_in = int(usage.get("prompt_tokens") or 0)
    tokens_out = int(usage.get("completion_tokens") or 0)
    return {"text": content, "tokens_in": tokens_in, "tokens_out": tokens_out}


def call_claude(system: str, user: str) -> dict:
    """Anthropic Messages API."""
    _require_credentials(need_key=True)
    url = API_BASE_URL or URL_CLAUDE
    data = post_json(
        url,
        {"x-api-key": API_KEY, "anthropic-version": "2023-06-01"},
        {
            "model": MODEL_NAME,
            "max_tokens": 1536,
            "temperature": 0.2,
            "system": system or "",
            "messages": [{"role": "user", "content": user}],
        },
    )
    text = "".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text")
    usage = data.get("usage") or {}
    return {
        "text": text,
        "tokens_in": int(usage.get("input_tokens") or 0),
        "tokens_out": int(usage.get("output_tokens") or 0),
    }


def call_ollama(system: str, user: str) -> dict:
    """Ollama chạy trên máy local."""
    _require_credentials(need_key=False)
    url = API_BASE_URL or URL_OLLAMA
    messages = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": user}]
    data = post_json(url, {}, {"model": MODEL_NAME, "messages": messages, "stream": False}, timeout=300)
    return {
        "text": (data.get("message") or {}).get("content", ""),
        "tokens_in": int(data.get("prompt_eval_count") or 0),
        "tokens_out": int(data.get("eval_count") or 0),
    }


@model_call
def call_model(system: str, user: str) -> dict:
    if MODEL_PROVIDER == "fake":
        last = (user.strip().splitlines() or [""])[-1]
        return {"text": "[câu trả lời giả — chưa nối model] " + last[:60], "model": "fake", "tokens_in": 0, "tokens_out": 0}
    if MODEL_PROVIDER in ("gemini", "google"):
        r = call_gemini(system, user)
    elif MODEL_PROVIDER in OPENAI_COMPAT_URLS:
        r = call_openai_compat(system, user, OPENAI_COMPAT_URLS[MODEL_PROVIDER])
    elif MODEL_PROVIDER in ("anthropic", "claude"):
        r = call_claude(system, user)
    elif MODEL_PROVIDER == "ollama":
        r = call_ollama(system, user)
    elif API_BASE_URL:
        r = call_openai_compat(system, user, API_BASE_URL)
    else:
        raise ValueError(
            "MODEL_PROVIDER=%r chưa hỗ trợ. Dùng một trong: fake, gemini, openai, groq, openrouter, deepseek, anthropic, ollama."
            % MODEL_PROVIDER
        )
    return {
        "text": r["text"],
        "model": MODEL_NAME,
        "tokens_in": int(r["tokens_in"]),
        "tokens_out": int(r["tokens_out"]),
    }

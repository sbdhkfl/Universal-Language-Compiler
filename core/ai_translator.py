"""Optional local-AI code generation for unrestricted English descriptions.

The deterministic compiler remains available. If a local Ollama server is running,
this module lets the browser accept much broader English programming requests without
using a paid cloud API.
"""
import json
import os
import re
import urllib.request
import urllib.error

OLLAMA_URL = os.getenv("ULC_OLLAMA_URL", "http://127.0.0.1:11434/api/generate")
OLLAMA_MODEL = os.getenv("ULC_OLLAMA_MODEL", "qwen2.5-coder:3b")

def clean_code(text: str) -> str:
    text = text.strip()
    match = re.search(r"```(?:\w+)?\s*(.*?)```", text, re.DOTALL)
    return match.group(1).strip() if match else text

def generate_with_local_ai(instruction: str, target: str) -> str:
    prompt = f"""You are the code-generation engine for Universal Language Compiler.
Convert the user's English programming request into a complete, runnable program in {target}.
Understand normal English, not only fixed command patterns.
Requirements:
- Return ONLY source code. No markdown fences and no explanation.
- Implement the requested behavior as completely as possible.
- Use standard libraries when practical.
- Include comments for important parts.
- Never include passwords, API keys, or private tokens.
- If the request is ambiguous, make a reasonable assumption and state it in a source-code comment.
- Do not intentionally create malware, credential theft, destructive payloads, or other harmful code.

User request:
{instruction}
"""
    payload = json.dumps({
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.2}
    }).encode("utf-8")
    req = urllib.request.Request(
        OLLAMA_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as response:
            data = json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError) as exc:
        raise RuntimeError(
            "Local AI is not running. Install/start Ollama and download the configured "
            f"model ({OLLAMA_MODEL}), or use one of the built-in simple instructions."
        ) from exc
    answer = data.get("response", "")
    if not answer:
        raise RuntimeError("The local AI returned no code.")
    return clean_code(answer)

"""Start and verify the local Ollama service for ULC."""
import os, shutil, subprocess, time, urllib.request

URL = os.getenv("ULC_OLLAMA_URL", "http://127.0.0.1:11434/api/tags")

def ollama_executable():
    found = shutil.which("ollama")
    if found:
        return found
    if os.name == "nt":
        for p in [
            os.path.expandvars(r"%LocalAppData%\Programs\Ollama\ollama.exe"),
            os.path.expandvars(r"%ProgramFiles%\Ollama\ollama.exe"),
        ]:
            if os.path.exists(p):
                return p
    return None

def server_ready():
    try:
        with urllib.request.urlopen(URL, timeout=2) as response:
            return response.status == 200
    except Exception:
        return False

def ensure_ollama():
    exe = ollama_executable()
    if not exe:
        return False, "Ollama is not installed. Run START.bat so it can install the local AI automatically."
    if not server_ready():
        try:
            flags = getattr(subprocess, "CREATE_NO_WINDOW", 0) if os.name == "nt" else 0
            subprocess.Popen([exe, "serve"], creationflags=flags,
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception as exc:
            return False, f"Could not start Ollama: {exc}"
        for _ in range(30):
            if server_ready():
                break
            time.sleep(1)
    if not server_ready():
        return False, "Ollama was found but its local server did not start."
    return True, ""

if __name__ == "__main__":
    ok, message = ensure_ollama()
    print("Local AI ready." if ok else message)

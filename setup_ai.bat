@echo off
setlocal
echo Universal Language Compiler - Local AI setup
where ollama >nul 2>nul
if errorlevel 1 (
  echo Ollama was not found. Trying to install it with Windows Package Manager...
  winget install --id Ollama.Ollama -e
)
echo.
echo Downloading the local coding model. This may take a while.
ollama pull qwen2.5-coder:3b
echo.
echo Setup finished. You can now run:
echo     python run.py
pause

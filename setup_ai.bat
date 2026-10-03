@echo off
setlocal EnableExtensions
cd /d "%~dp0"

echo Universal Language Compiler - Local AI setup
echo.

where ollama >nul 2>nul
if errorlevel 1 (
  if exist "%LocalAppData%\Programs\Ollama\ollama.exe" (
    set "PATH=%LocalAppData%\Programs\Ollama;%PATH%"
  ) else (
    echo Ollama was not found. Installing it...
    where winget >nul 2>nul
    if errorlevel 1 (
      echo winget is not available. Install Ollama once, then run this file again.
      pause
      exit /b 1
    )
    winget install --id Ollama.Ollama -e --scope user --accept-source-agreements --accept-package-agreements
    if errorlevel 1 (
      echo Ollama installation failed.
      pause
      exit /b 1
    )
    if exist "%LocalAppData%\Programs\Ollama\ollama.exe" set "PATH=%LocalAppData%\Programs\Ollama;%PATH%"
  )
)

where ollama >nul 2>nul
if errorlevel 1 (
  echo Ollama is installed but not available in this window yet.
  echo Close this window, wait a few seconds, and run setup_ai.bat again.
  pause
  exit /b 1
)

echo Starting the local AI server...
curl.exe -s http://127.0.0.1:11434/api/tags >nul 2>nul
if errorlevel 1 (
  start "" /b ollama serve > "%TEMP%\ulc_ollama.log" 2>&1
  timeout /t 3 /nobreak >nul
)

echo Downloading the local coding model if needed...
ollama pull qwen2.5-coder:3b

echo.
echo Local AI setup finished.
echo You can now double-click START.bat.
pause

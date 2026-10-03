@echo off
setlocal EnableExtensions
cd /d "%~dp0"

echo Starting Universal Language Compiler...
where py >nul 2>nul
if errorlevel 1 (
  where python >nul 2>nul
  if errorlevel 1 (
    echo Python not found. Installing Python 3.12...
    winget install --id Python.Python.3.12 -e --scope user --accept-source-agreements --accept-package-agreements
    if errorlevel 1 (
      echo Python installation failed.
      pause
      exit /b 1
    )
  )
)

python -m pip install -e .

where ollama >nul 2>nul
if errorlevel 1 if exist "%LocalAppData%\Programs\Ollama\ollama.exe" set "PATH=%LocalAppData%\Programs\Ollama;%PATH%"
where ollama >nul 2>nul
if errorlevel 1 (
  echo Ollama not found. Installing automatically...
  winget install --id Ollama.Ollama -e --scope user --accept-source-agreements --accept-package-agreements
  if errorlevel 1 (
    echo Ollama installation failed.
    pause
    exit /b 1
  )
  set "PATH=%LocalAppData%\Programs\Ollama;%PATH%"
)

echo Starting local AI...
python -m core.local_ai_manager
if errorlevel 1 echo Local AI startup check failed. The browser will still open.

echo Opening Chrome...
python run.py
pause

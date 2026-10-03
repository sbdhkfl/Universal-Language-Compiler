@echo off
setlocal EnableExtensions
cd /d "%~dp0"

echo.
echo ==========================================
echo        PROJECT STARTER
echo ==========================================
echo.

where py >nul 2>nul
if not errorlevel 1 goto PYTHON_OK

where python >nul 2>nul
if not errorlevel 1 goto PYTHON_OK

echo Python was not found. Installing Python 3.12 for your Windows user...
where winget >nul 2>nul
if errorlevel 1 (
  echo.
  echo Windows Package Manager (winget) is not available.
  echo Please install Python 3.12 once, then run this file again.
  pause
  exit /b 1
)
winget install --id Python.Python.3.12 -e --scope user --accept-source-agreements --accept-package-agreements
if errorlevel 1 (
  echo Python installation failed.
  pause
  exit /b 1
)

set "PATH=%LocalAppData%\Programs\Python\Python312;%LocalAppData%\Programs\Python\Python312\Scripts;%PATH%"

:PYTHON_OK
python --version
python -m pip install --upgrade pip

echo Installing the Universal Language Compiler...
python -m pip install -e .

echo.
echo Checking for Ollama...
where ollama >nul 2>nul
if errorlevel 1 (
  echo Installing Ollama...
  winget install --id Ollama.Ollama -e --scope user --accept-source-agreements --accept-package-agreements
)

where ollama >nul 2>nul
if not errorlevel 1 (
  echo.
  echo Downloading the local coding model if needed...
  ollama pull qwen2.5-coder:3b
)

echo.
echo Starting Universal Language Compiler...
python run.py
pause

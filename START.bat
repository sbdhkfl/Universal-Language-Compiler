@echo off
setlocal EnableExtensions
cd /d "%~dp0"

echo.
echo ==========================================
echo   UNIVERSAL LANGUAGE COMPILER STARTER
echo ==========================================
echo.

REM Find Python
where py >nul 2>nul
if not errorlevel 1 goto PYTHON_OK
where python >nul 2>nul
if not errorlevel 1 goto PYTHON_OK

echo Python was not found. Installing Python 3.12 for your Windows user...
where winget >nul 2>nul
if errorlevel 1 (
  echo Windows Package Manager (winget) is not available.
  echo Please install Python 3.12 once, then run START.bat again.
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
python -m pip install -e .

REM Find Ollama, including its normal per-user Windows install folder.
where ollama >nul 2>nul
if not errorlevel 1 goto OLLAMA_FOUND
if exist "%LocalAppData%\Programs\Ollama\ollama.exe" (
  set "PATH=%LocalAppData%\Programs\Ollama;%PATH%"
  goto OLLAMA_FOUND
)

echo.
echo Ollama was not found. Installing it...
where winget >nul 2>nul
if errorlevel 1 (
  echo winget is not available, so Ollama cannot be installed automatically.
  echo Install Ollama once, then run START.bat again.
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

:OLLAMA_FOUND
where ollama >nul 2>nul
if errorlevel 1 (
  echo Ollama was installed but Windows has not made it available yet.
  echo Close this window, wait a few seconds, and double-click START.bat again.
  pause
  exit /b 1
)

echo.
echo Checking the local AI server...
curl.exe -s http://127.0.0.1:11434/api/tags >nul 2>nul
if errorlevel 1 (
  echo Starting Ollama in the background...
  start "" /b ollama serve > "%TEMP%\ulc_ollama.log" 2>&1
  timeout /t 3 /nobreak >nul
)

echo Checking the coding model...
ollama list | findstr /i "qwen2.5-coder:3b" >nul 2>nul
if errorlevel 1 (
  echo Downloading qwen2.5-coder:3b. This may take a while the first time.
  ollama pull qwen2.5-coder:3b
  if errorlevel 1 (
    echo.
    echo The local AI model could not be downloaded.
    echo Check %TEMP%\ulc_ollama.log for Ollama details.
    pause
    exit /b 1
  )
)

echo.
echo Starting Universal Language Compiler...
python run.py
pause

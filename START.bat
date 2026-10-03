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
if errorlevel 1 (
  echo Project installation failed.
  pause
  exit /b 1
)

echo Starting translator...
python run.py
pause

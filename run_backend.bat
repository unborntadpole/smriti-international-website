@echo off
echo Starting project...

REM Create venv if not exists
if not exist .venv (
    echo Creating virtual environment...
    python -m venv .venv
)

REM Activate venv
echo Activating virtual environment...
call .venv\Scripts\activate

REM Install Python deps
echo Installing Python dependencies...
pip install -r requirements.txt

REM Start backend in new window with venv activated
echo Starting backend...
start cmd /k "call .venv\Scripts\activate && cd backend && python main.py"

echo Everything is running!
pause
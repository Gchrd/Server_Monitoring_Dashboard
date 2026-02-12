@echo off
echo Starting Server Monitoring System...

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH.
    pause
    exit /b
)

REM Check if Node is installed
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Node.js is not installed or not in PATH.
    pause
    exit /b
)

echo Launching Agent...
start "Monitoring Agent" cmd /k "cd agent && python monitor.py"

echo Launching Backend...
start "Backend API" cmd /k "cd backend && uvicorn main:app --reload"

echo Launching Frontend...
start "Frontend Dashboard" cmd /k "cd frontend && npm run dev"

echo All components launched! 
echo Please ensure your database is running and configured in .env
pause

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv
from datetime import datetime

# Load env from root
load_dotenv(dotenv_path='../.env')

app = FastAPI()

# CORS config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow all for dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class LogEntry(BaseModel):
    id: int
    server_name: str
    cpu_usage: float
    ram_usage: float
    disk_usage: float
    status: str
    created_at: datetime

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            port=os.getenv('DB_PORT')
        )
        return conn
    except Exception as e:
        print(f"DB Connection failed: {e}")
        return None

@app.get("/")
def read_root():
    return {"message": "Server Monitoring API is running"}

@app.get("/stats/current", response_model=LogEntry)
def get_current_stats():
    conn = get_db_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Database connection error")
    
    cur = conn.cursor()
    cur.execute("SELECT id, server_name, cpu_usage, ram_usage, disk_usage, status, created_at FROM server_logs ORDER BY created_at DESC LIMIT 1")
    row = cur.fetchone()
    cur.close()
    conn.close()

    if row:
        return LogEntry(
            id=row[0], server_name=row[1], cpu_usage=row[2], 
            ram_usage=row[3], disk_usage=row[4], status=row[5], created_at=row[6]
        )
    else:
        raise HTTPException(status_code=404, detail="No logs found")

@app.get("/stats/history", response_model=List[LogEntry])
def get_history_stats():
    conn = get_db_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Database connection error")
        
    cur = conn.cursor()
    # Get last 60 entries (approx 5 mins if logging every 5s)
    cur.execute("SELECT id, server_name, cpu_usage, ram_usage, disk_usage, status, created_at FROM server_logs ORDER BY created_at DESC LIMIT 60")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Reformat for charts (oldest to newest)
    history = []
    for row in rows:
        history.append(LogEntry(
            id=row[0], server_name=row[1], cpu_usage=row[2], 
            ram_usage=row[3], disk_usage=row[4], status=row[5], created_at=row[6]
        ))
    return history[::-1] # Reverse to have oldest first

@app.get("/stats/logs", response_model=List[LogEntry])
def get_recent_logs():
    conn = get_db_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Database connection error")
        
    cur = conn.cursor()
    cur.execute("SELECT id, server_name, cpu_usage, ram_usage, disk_usage, status, created_at FROM server_logs ORDER BY created_at DESC LIMIT 20")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    logs = []
    for row in rows:
        logs.append(LogEntry(
            id=row[0], server_name=row[1], cpu_usage=row[2], 
            ram_usage=row[3], disk_usage=row[4], status=row[5], created_at=row[6]
        ))
    return logs

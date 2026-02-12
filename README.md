# Server Monitoring Dashboard

A full-stack implementation of a Server Monitoring System using **Python**, **PostgreSQL**, **FastAPI**, and **Vue.js**.

## Concept & Architecture

This project simulates a real-world infrastructure monitoring system. It consists of three decoupled components:

1.  **The Agent (`agent/monitor.py`)**: 
    - A lightweight Python script designed to run on *target servers*.
    - It collects system metrics (CPU, RAM, Disk) using `psutil`.
    - It sends data to the centralized database.
    - *In this demo, your local machine acts as the "Server" being monitored.*

2.  **The Central Database (PostgreSQL)**:
    - Stores time-series data of server health logs.
    - Built to handle high-frequency writes from the agent.

3.  **The Dashboard (Backend + Frontend)**:
    - **Backend (FastAPI)**: Provides a secure REST API to query the logs.
    - **Frontend (Vue.js)**: Visualize the data in real-time using interactive charts.

---

## Tech Stack

-   **System**: Python (`psutil`)
-   **Database**: PostgreSQL
-   **API**: FastAPI (`Python`)
-   **Frontend**: Vue.js + Vite
-   **Visuals**: Chart.js

---

## How to Run

### 1. Database Setup
Ensure PostgreSQL is running and create a database (e.g., `monitoring_db`).
```sql
-- Run the schema script provided in database/schema.sql
CREATE TABLE server_logs (...);
```
Configure your `.env` file based on `.env.example`.

### 2. Install Dependencies
```bash
# Agent & Backend
pip install -r agent/requirements.txt
pip install -r backend/requirements.txt

# Frontend
cd frontend
npm install
```

### 3. Launch System
Double-click **`start.bat`** (Windows) to launch all components simultaneously.

Alternatively, run manually:
1.  `python agent/monitor.py`
2.  `uvicorn backend.main:app --reload`
3.  `npm run dev` (in frontend dir)

---

## Scalability Note
To monitor **multiple servers**, you simply deploy the `agent/` folder to other machines and configure their `.env` to point to this central database. The dashboard will then receive data from all connected servers.

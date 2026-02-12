import psutil
import time
import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from the root .env file
load_dotenv(dotenv_path='../.env')

# Database Connection Helper
def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        port=os.getenv('DB_PORT')
    )
    return conn

def determine_status(cpu, ram, disk):
    if cpu > 80 or ram > 85 or disk > 90:
        return 'Critical'
    elif cpu > 50 or ram > 60 or disk > 70:
        return 'Warning'
    else:
        return 'Healthy'

def monitor_system():
    print("Starting Server Monitoring Agent...")
    try:
        while True:
            # Gather Metrics
            cpu = psutil.cpu_percent(interval=1)
            ram = psutil.virtual_memory().percent
            disk = psutil.disk_usage('/').percent
            status = determine_status(cpu, ram, disk)
            
            # Log to Console
            print(f"CPU: {cpu}%, RAM: {ram}%, Disk: {disk}%, Status: {status}")

            # Insert into DB
            try:
                conn = get_db_connection()
                cur = conn.cursor()
                cur.execute(
                    "INSERT INTO server_logs (server_name, cpu_usage, ram_usage, disk_usage, status) VALUES (%s, %s, %s, %s, %s)",
                    ('LocalServer', cpu, ram, disk, status)
                )
                conn.commit()
                cur.close()
                conn.close()
            except Exception as e:
                print(f"Error logging to database: {e}")

            # Wait before next check
            time.sleep(4) 
    except KeyboardInterrupt:
        print("Monitoring Agent Stopped.")

if __name__ == "__main__":
    monitor_system()

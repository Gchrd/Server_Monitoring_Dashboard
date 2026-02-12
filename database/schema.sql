CREATE TABLE IF NOT EXISTS server_logs (
    id SERIAL PRIMARY KEY,
    server_name VARCHAR(50),
    cpu_usage FLOAT,          
    ram_usage FLOAT,          
    disk_usage FLOAT,         
    status VARCHAR(20),       
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

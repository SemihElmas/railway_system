# GÖREV: Database Readiness Health Check Endpoint (SCRUM-106)
import sqlite3
from datetime import datetime

def check_db_readiness(db_path="railway.db"):
    """
    controls the readiness of the database connection by attempting to connect and execute a simple query.
    If the connection is successful and the query executes without errors, it returns a status of "ready". 
    If there is an issue with the database connection, it catches the exception and returns a status of "loading" along with the error message. This allows the system to report its health status accurately without crashing if the database is not yet available.
    """
    try:
        # try to connect to the database and execute a simple query to ensure it's responsive
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # check if we can execute a simple query to confirm the database is responsive
        cursor.execute("SELECT 1;")
        cursor.fetchone()
        conn.close()
        
        return {
            "status": "ready",
            "database": "connected",
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        # rapor any exceptions that occur during the database connection attempt, indicating that the database is not ready
        return {
            "status": "loading",
            "database": "disconnected",
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }
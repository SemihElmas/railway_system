# GÖREV: Database Backup and Export Utility (SCRUM-127)
import os
import sqlite3
from datetime import datetime

def backup_database(db_path="railway.db", backup_dir="backups"):
    """
    takes a snapshot of the current state of the database by creating a backup copy of the database file.
    """
    # dont proceed if the source database file does not exist
    if not os.path.exists(db_path):
        return {"status": "error", "message": f"Source database '{db_path}' not found."}
        
    # create the backup directory if it doesn't exist
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
        
    # create a timestamped backup filename to avoid overwriting previous backups
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"railway_backup_{timestamp}.db")
    
    try:
        # don't just copy the file, use sqlite3's backup API to ensure a consistent snapshot even if the database is in use
        with sqlite3.connect(db_path) as src_conn:
            with sqlite3.connect(backup_path) as dest_conn:
                src_conn.backup(dest_conn)
        
        return {
            "status": "success",
            "message": "Database snapshot created successfully.",
            "backup_file": backup_path
        }
    except Exception as e:
        return {
            "status": "failed",
            "error": str(e)
        }
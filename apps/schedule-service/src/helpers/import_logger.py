import time

def log_import_summary(rows_processed, start_time):
    execution_time = round(time.time() - start_time, 4)
    return {
        "status": "SUCCESS",
        "records_imported": rows_processed,
        "duration_seconds": execution_time,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
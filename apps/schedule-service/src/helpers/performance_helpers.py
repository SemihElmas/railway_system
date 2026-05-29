# GÖREV: Implement search query performance tracker (SCRUM-34)
import time

def track_search_performance(start_time):
    """
    prints the execution time of a route search query in milliseconds and returns the execution time for further analysis or logging.
    """
    # transform the execution time to milliseconds for better readability in performance logs
    execution_time_ms = (time.time() - start_time) * 1000
    
    print(f"[PERF] Route search query executed in {execution_time_ms:.2f} ms")
    
    return execution_time_ms
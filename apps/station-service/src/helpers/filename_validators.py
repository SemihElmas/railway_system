#Implement input filename sanitization for CSV uploads (SCRUM-45)
import os

def sanitize_csv_filename(filename):
    """
    cleans the input filename by removing leading/trailing spaces, replacing internal spaces with underscores, converting to lowercase, and removing special characters except for underscores and alphanumeric characters.
    This ensures that the filename is safe and consistent for storage and processing in the system.
    """
    
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(base_name)
    
    clean_name = name.strip().replace(" ", "_").lower()
    
    clean_name = "".join(c for c in clean_name if c.isalnum() or c == "_")
    
    return f"{clean_name}{ext}"
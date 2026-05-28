def validate_polish_coordinates(latitude, longitude):
    LAT_MIN, LAT_MAX = 49.0, 55.0
    LON_MIN, LON_MAX = 14.0, 25.0
    try:
        lat, lon = float(latitude), float(longitude)
    except (ValueError, TypeError):
        return False, "Coordinates must be numbers."
    if not (LAT_MIN <= lat <= LAT_MAX) or not (LON_MIN <= lon <= LON_MAX):
        return False, "Outside Poland borders."
    return True, "Valid Polish coordinates."
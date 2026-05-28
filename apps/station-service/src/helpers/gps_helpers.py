import math
from database import get_connection


def get_station_with_coordinates(station_id: int):
    conn = get_connection()
    station = conn.execute(
        "SELECT id, name, city, lat, lon FROM stations WHERE id = ?",
        (station_id,)
    ).fetchone()
    conn.close()
    return dict(station) if station else None


def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(math.radians(lat1)) *
         math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return round(R * c, 2)


def get_all_stations_with_coordinates():
    conn = get_connection()
    stations = conn.execute(
        "SELECT id, name, city, lat, lon FROM stations"
    ).fetchall()
    conn.close()
    return [dict(s) for s in stations]
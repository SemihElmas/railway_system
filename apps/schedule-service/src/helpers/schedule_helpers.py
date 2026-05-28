from database import get_connection


def create_schedule(from_station_id: int, to_station_id: int,
                    departure_time: str, arrival_time: str,
                    recurrence: str, price: float) -> dict:
    conn = get_connection()
    cursor = conn.cursor()

    existing = conn.execute("""
        SELECT id FROM schedules 
        WHERE from_station_id = ? 
        AND to_station_id = ? 
        AND departure_time = ?
    """, (from_station_id, to_station_id, departure_time)).fetchone()

    if existing:
        conn.close()
        return {"error": "Schedule already exists for this route and time"}

    cursor.execute("""
        INSERT INTO schedules 
        (from_station_id, to_station_id, departure_time, arrival_time, recurrence, price)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (from_station_id, to_station_id, departure_time, arrival_time, recurrence, price))

    conn.commit()
    schedule_id = cursor.lastrowid
    conn.close()
    return {"id": schedule_id, "message": "Schedule created successfully"}


def get_all_schedules() -> list:
    conn = get_connection()
    schedules = conn.execute("SELECT * FROM schedules").fetchall()
    conn.close()
    return [dict(s) for s in schedules]


def validate_recurrence(recurrence: str) -> bool:
    return recurrence in ["daily", "weekly"]
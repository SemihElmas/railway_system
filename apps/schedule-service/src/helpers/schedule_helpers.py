schedules_db = []


def create_schedule(from_station_id: int, to_station_id: int,
                   departure_time: str, arrival_time: str,
                   recurrence: str, price: float) -> dict:
    existing = [s for s in schedules_db if
                s["from_station_id"] == from_station_id and
                s["to_station_id"] == to_station_id and
                s["departure_time"] == departure_time]
    if existing:
        return {"error": "Schedule already exists for this route and time"}

    schedule = {
        "id": len(schedules_db) + 1,
        "from_station_id": from_station_id,
        "to_station_id": to_station_id,
        "departure_time": departure_time,
        "arrival_time": arrival_time,
        "recurrence": recurrence,
        "price": price
    }
    schedules_db.append(schedule)
    return {"id": schedule["id"], "message": "Schedule created successfully"}


def get_all_schedules() -> list:
    return schedules_db


def validate_recurrence(recurrence: str) -> bool:
    return recurrence in ["daily", "weekly"]
def filter_connections_by_time(connections: list, time_of_day: str = None) -> list:
    if not time_of_day:
        return connections
    return [c for c in connections if c["departure_time"].startswith(time_of_day)]


def validate_search_input(from_city: str, to_city: str) -> bool:
    if not from_city or not to_city:
        return False
    if from_city.lower() == to_city.lower():
        return False
    return True


def format_connection_result(connections: list) -> dict:
    if not connections:
        return {"message": "No connections found", "connections": []}
    return {"message": f"{len(connections)} connections found", "connections": connections}
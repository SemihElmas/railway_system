import uvicorn
import httpx
from fastapi import FastAPI

app = FastAPI()

STATION_SERVICE_URL = "http://station-service:8000"


@app.get("/")
def root():
    return {"message": "Schedule Service is running"}


@app.get("/connections")
async def search_connections(from_city: str, to_city: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{STATION_SERVICE_URL}/stations")
        stations = response.json()

    from_stations = [s for s in stations if s["city"].lower() == from_city.lower()]
    to_stations = [s for s in stations if s["city"].lower() == to_city.lower()]

    if not from_stations or not to_stations:
        return {"message": "No connections found", "connections": []}

    connections = []
    for f in from_stations:
        for t in to_stations:
            connections.append({
                "from": f["name"],
                "to": t["name"],
                "from_city": f["city"],
                "to_city": t["city"],
                "departure_time": "08:00",
                "arrival_time": "10:30",
                "price": 49.99,
                "recurrence": "daily"
            })

    return {"connections": connections}

from pydantic import BaseModel
from helpers.search_helpers import validate_search_input, format_connection_result
from helpers.schedule_helpers import create_schedule, get_all_schedules, validate_recurrence


class ScheduleRequest(BaseModel):
    from_station_id: int
    to_station_id: int
    departure_time: str
    arrival_time: str
    recurrence: str = "daily"
    price: float


@app.post("/schedules")
def add_schedule(schedule: ScheduleRequest):
    if not validate_recurrence(schedule.recurrence):
        return {"error": "Recurrence must be 'daily' or 'weekly'"}
    result = create_schedule(
        schedule.from_station_id,
        schedule.to_station_id,
        schedule.departure_time,
        schedule.arrival_time,
        schedule.recurrence,
        schedule.price
    )
    return result


@app.get("/schedules")
def list_schedules():
    return get_all_schedules()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
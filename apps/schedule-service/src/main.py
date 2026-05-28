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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import init_db, get_connection

app = FastAPI()


@app.on_event("startup")
def startup():
    init_db()


class Station(BaseModel):
    name: str
    city: str
    platform_count: int
    lat: float
    lon: float


@app.get("/")
def root():
    return {"message": "Station Service is running"}


@app.get("/stations")
def get_stations():
    conn = get_connection()
    stations = conn.execute("SELECT * FROM stations").fetchall()
    conn.close()
    return [dict(s) for s in stations]


@app.get("/stations/{station_id}")
def get_station(station_id: int):
    conn = get_connection()
    station = conn.execute(
        "SELECT * FROM stations WHERE id = ?", (station_id,)
    ).fetchone()
    conn.close()
    if not station:
        raise HTTPException(status_code=404, detail="Station not found")
    return dict(station)


@app.post("/stations")
def create_station(station: Station):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO stations (name, city, platform_count, lat, lon) VALUES (?, ?, ?, ?, ?)",
        (station.name, station.city, station.platform_count, station.lat, station.lon)
    )
    conn.commit()
    station_id = cursor.lastrowid
    conn.close()
    return {"id": station_id, **station.dict()}


@app.delete("/stations/{station_id}")
def delete_station(station_id: int):
    conn = get_connection()
    conn.execute("DELETE FROM stations WHERE id = ?", (station_id,))
    conn.commit()
    conn.close()
    return {"message": "Station deleted"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
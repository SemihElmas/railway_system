import sqlite3
import os

DB_PATH = os.getenv("DB_PATH", "/app/data/railway.db")


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            city TEXT NOT NULL,
            platform_count INTEGER NOT NULL,
            lat REAL NOT NULL,
            lon REAL NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS schedules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            from_station_id INTEGER NOT NULL,
            to_station_id INTEGER NOT NULL,
            departure_time TEXT NOT NULL,
            arrival_time TEXT NOT NULL,
            recurrence TEXT NOT NULL DEFAULT 'daily',
            price REAL NOT NULL,
            FOREIGN KEY (from_station_id) REFERENCES stations(id),
            FOREIGN KEY (to_station_id) REFERENCES stations(id)
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM stations")
    if cursor.fetchone()[0] == 0:
        stations = [
            ("Warszawa Centralna", "Warszawa", 8, 52.2286, 21.0031),
            ("Kraków Główny", "Kraków", 6, 50.0675, 19.9478),
            ("Gdańsk Główny", "Gdańsk", 5, 54.3565, 18.6438),
            ("Wrocław Główny", "Wrocław", 6, 51.0973, 17.0386),
            ("Poznań Główny", "Poznań", 7, 52.4058, 16.9250),
        ]
        cursor.executemany(
            "INSERT INTO stations (name, city, platform_count, lat, lon) VALUES (?, ?, ?, ?, ?)",
            stations
        )

    conn.commit()
    conn.close()
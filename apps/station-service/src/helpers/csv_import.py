import csv
import io
from database import get_connection


def import_stations_from_csv(content: str) -> dict:
    conn = get_connection()
    cursor = conn.cursor()

    imported = 0
    errors = 0
    reader = csv.DictReader(io.StringIO(content))

    for row in reader:
        try:
            if not row.get("name") or not row.get("city"):
                errors += 1
                continue
            cursor.execute(
                "INSERT INTO stations (name, city, platform_count, lat, lon) VALUES (?, ?, ?, ?, ?)",
                (
                    row["name"],
                    row["city"],
                    int(row["platform_count"]),
                    float(row["lat"]),
                    float(row["lon"])
                )
            )
            imported += 1
        except Exception:
            errors += 1

    conn.commit()
    conn.close()
    return {"imported": imported, "errors": errors}
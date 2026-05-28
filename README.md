# Railway System - Train and Station Information

## Services
- **station-service** (port 8001) - manages stations, GPS coordinates, CSV import
- **schedule-service** (port 8000) - searches connections, manages recurring schedules

## How to run
```bash
docker-compose up
```

## Endpoints
### Station Service (http://localhost:8001)
- GET /stations - list all stations
- POST /stations - add station
- DELETE /stations/{id} - delete station
- POST /import-csv - import stations from CSV file

### Schedule Service (http://localhost:8000)
- GET /connections?from_city=Warszawa&to_city=Kraków - search connections
- GET /schedules - list all schedules
- POST /schedules - create recurring schedule

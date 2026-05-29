def transform_to_geojson(station_name, lat, lon):
    if not station_name or lat is None or lon is None:
        return {"error": "Invalid database record"}
    return {
        "type": "Feature",
        "properties": {"station_name": station_name, "country": "Poland"},
        "geometry": {"type": "Point", "coordinates": [float(lon), float(lat)]}
    }
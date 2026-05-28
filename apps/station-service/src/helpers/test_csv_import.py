from helpers.csv_import import import_stations_from_csv


def test_import_valid_csv():
    csv_content = """name,city,platform_count,lat,lon
Warszawa Centralna,Warszawa,8,52.2286,21.0031
Kraków Główny,Kraków,6,50.0675,19.9478"""
    result = import_stations_from_csv(csv_content)
    assert result["imported"] == 2
    assert result["errors"] == 0


def test_import_invalid_row():
    csv_content = """name,city,platform_count,lat,lon
,Warszawa,8,52.2286,21.0031"""
    result = import_stations_from_csv(csv_content)
    assert result["imported"] == 0
    assert result["errors"] == 1


def test_import_mixed_rows():
    csv_content = """name,city,platform_count,lat,lon
Gdańsk Główny,Gdańsk,5,54.3565,18.6438
,Łódź,6,51.7769,19.4664"""
    result = import_stations_from_csv(csv_content)
    assert result["imported"] == 1
    assert result["errors"] == 1
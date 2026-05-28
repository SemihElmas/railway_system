from helpers.station_helpers import calculate_distance, validate_coordinates, validate_station


def test_calculate_distance_between_warsaw_and_krakow():
    distance = calculate_distance(52.2286, 21.0031, 50.0675, 19.9478)
    assert distance > 0


def test_validate_coordinates_valid():
    assert validate_coordinates(52.2286, 21.0031) is True


def test_validate_coordinates_invalid():
    assert validate_coordinates(200, 300) is False


def test_validate_station_valid():
    assert validate_station("Warszawa Centralna", "Warszawa", 8) is True


def test_validate_station_invalid():
    assert validate_station("", "Warszawa", 8) is False
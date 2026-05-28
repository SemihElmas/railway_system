from helpers.gps_helpers import calculate_distance


def test_calculate_distance_returns_positive():
    distance = calculate_distance(52.2286, 21.0031, 50.0675, 19.9478)
    assert distance > 0


def test_calculate_distance_warsaw_krakow():
    distance = calculate_distance(52.2286, 21.0031, 50.0675, 19.9478)
    assert 250 < distance < 300


def test_calculate_distance_same_point():
    distance = calculate_distance(52.2286, 21.0031, 52.2286, 21.0031)
    assert distance == 0.0
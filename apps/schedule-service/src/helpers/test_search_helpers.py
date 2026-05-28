from helpers.search_helpers import validate_search_input, format_connection_result, filter_connections_by_time


def test_validate_search_input_valid():
    assert validate_search_input("Warszawa", "Kraków") is True


def test_validate_search_input_empty():
    assert validate_search_input("", "Kraków") is False


def test_validate_search_input_same_city():
    assert validate_search_input("Warszawa", "Warszawa") is False


def test_format_connection_result_empty():
    result = format_connection_result([])
    assert result["message"] == "No connections found"


def test_format_connection_result_with_data():
    connections = [{"from": "Warszawa", "to": "Kraków"}]
    result = format_connection_result(connections)
    assert "1 connections found" in result["message"]


def test_filter_connections_by_time():
    connections = [
        {"departure_time": "08:00"},
        {"departure_time": "12:00"}
    ]
    result = filter_connections_by_time(connections, "08")
    assert len(result) == 1
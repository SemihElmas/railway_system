from helpers.schedule_helpers import validate_recurrence


def test_validate_recurrence_daily():
    assert validate_recurrence("daily") is True


def test_validate_recurrence_weekly():
    assert validate_recurrence("weekly") is True


def test_validate_recurrence_invalid():
    assert validate_recurrence("monthly") is False


def test_validate_recurrence_empty():
    assert validate_recurrence("") is False
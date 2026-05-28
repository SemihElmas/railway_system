def format_coordinate_precision(value, decimal_places=4):
    try:
        return round(float(value), decimal_places)
    except (ValueError, TypeError):
        raise ValueError("Input must be a valid float-convertible value.")
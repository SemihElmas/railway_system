# task: Add price validation for recurring schedules (SCRUM-30)

def validate_schedule_price(price):
    """
    validates the price of a schedule to ensure it is a non-negative number.
    """
    try:
        fare = float(price)
        if fare < 0.0:
            raise ValueError("Ticket fare cannot be negative.")
        return True
    except (TypeError, ValueError):
      
        return False
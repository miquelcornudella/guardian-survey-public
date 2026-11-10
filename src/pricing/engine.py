# INTERNAL ONLY - fictional test code (guardian survey)
FLOOR_PRICE_EUR = 18.0  # Project Falcon pricing floor (fictional)

def quote(seats: int) -> float:
    """Fictional pricing rule: volume discount above 100 seats."""
    price = FLOOR_PRICE_EUR * seats
    return price * 0.85 if seats > 100 else price

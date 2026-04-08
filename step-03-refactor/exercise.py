def apply_discount(amount: float, pct: float) -> float:
    """Apply a discount percentage to an amount and return the discounted value."""
    if pct <= 0:
        return round(amount, 2)
    
    discount = amount * (pct / 100)
    total = amount - discount
    if total < 0:
        total = 0
    return round(total, 2)


def checkout_total(items: list[float], discount_percent: float) -> float:
    subtotal = 0.0
    for value in items:
        subtotal += value
    return apply_discount(subtotal, discount_percent)


def invoice_total(lines: list[float], discount_percent: float) -> float:
    subtotal = 0.0
    for value in lines:
        subtotal += value
    return apply_discount(subtotal, discount_percent)
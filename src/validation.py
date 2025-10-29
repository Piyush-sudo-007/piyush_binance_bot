import re

SYMBOL_RE = re.compile(r'^[A-Z0-9_]{3,12}$')

def validate_symbol(symbol: str) -> str:
    s = symbol.strip().upper()
    if not SYMBOL_RE.match(s):
        raise ValueError(f"Invalid symbol: {symbol}")
    return s

def validate_positive_number(value) -> float:
    try:
        v = float(value)
    except (TypeError, ValueError):
        raise ValueError('Quantity/price must be numeric')
    if v <= 0:
        raise ValueError('Quantity/price must be > 0')
    return v

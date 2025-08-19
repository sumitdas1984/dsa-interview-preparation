# Parse YYYY-MM-DD with validation for month/day ranges

# Option 1: Use datetime.strptime
from datetime import datetime

def parse_yyyy_mm_dd(s: str):
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()  # validates month/day & leap years
    except ValueError:
        return None  # invalid date

print(parse_yyyy_mm_dd("2025-22-28"))
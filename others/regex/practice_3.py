# Mask all but last 4 digits of card numbers in a string.

import re

def mask_card_numbers(text):
    # Match sequences of exactly 16 digits (with optional spaces or dashes)
    # return re.sub(r"\b(\d{12})(\d{4})\b", lambda m: "*" * 12 + m.group(2), text)
    re.sub(r"\b(\d{12})(\d{4})\b", "************\\2", text)

s = "My cards are 1234567812345678 and 9876543210987654."
print(mask_card_numbers(s))


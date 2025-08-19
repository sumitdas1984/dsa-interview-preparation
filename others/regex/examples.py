# Overview
# - re supports search, match, findall, sub, compile.
# - Use raw strings r"...". Pre-compile for performance in loops.
# - Useful features: groups, named groups, non-capturing (?:), lookarounds (?=...), (?!...).

import re

# email_pat = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
# l = email_pat.findall("contact me a@b.com or test@mail.io")
# print(l)

# # Named groups
# m = re.search(r"(?P<area>\d{3})-(?P<num>\d{7})", "Call 080-1234567")
# print(m.group("area"), m.group("num"))

# # Substitution
# result = re.sub(r"\s+", " ", "Too   many   spaces")
# print(result)

# search
text = "My phone number is 123-456-7890 and his number is 098-765-4321"
match = re.search(r"\d{3}-\d{3}-\d{4}", text)

if match:
    print("Found:", match.group())
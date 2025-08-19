# Extract all IPv4 addresses from text.

import re

text = "My ip is 123.17.8.1"
ipv4_pattern = re.compile(r'[0-255]')
l = ipv4_pattern.findall(text)
print(l)

import re

from_example = str()

with open("example.txt", "r") as file:
    from_example = file.read()

# 4 task
from_example = "This is simple exapmple, with_comma_and_dots."
output = re.sub(r'_(.)', lambda match: match.group(1).upper(), from_example)

print(output)

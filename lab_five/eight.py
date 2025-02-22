import re

from_example = str()

with open("example.txt", "r") as file:
    from_example = file.read()

# 8 task
from_example = "ThisIsSimpleExample,WithCommaAndDots."
output = re.split(r'(?=[A-Z])', from_example)
print(output)

import re

from_example = str()

with open("example.txt", "r") as file:
    from_example = file.read()

# 9 task
from_example = "ThisIsSimpleExample,WithCommaAndDots."
output = re.sub(r'(?<!^)(?=[A-Z])', ' ', from_example)

print(output)

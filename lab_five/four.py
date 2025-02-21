import re

from_example = str()

with open("example.txt", "r") as file:
    from_example = file.read()

# 4 task
output = re.findall("[A-Z][a-z]+", from_example)
print(output)

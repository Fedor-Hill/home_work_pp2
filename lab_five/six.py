import re

from_example = str()

with open("example.txt", "r") as file:
    from_example = file.read()

# 6 task
# from_example = "This is simple exapmple, with comma and dots."
output = re.sub(r'[ ,.]', ':', from_example)
print(output)

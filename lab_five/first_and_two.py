import re 

from_example = str()

with open("example.txt", "r") as file:
    from_example = file.read()

# 1 task
output = re.findall("a(b*)", from_example)

print(output)

# 2 task
output = re.findall("a(b{2,3})", from_example)

print(output)

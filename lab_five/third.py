import re

from_example = str()

with open("example.txt", "r") as file:
    from_example = file.read()

# from_example = "this a test with under_score_epta "
output = re.findall( r'[a-z]+_[a-z_]+', from_example)

print(output)

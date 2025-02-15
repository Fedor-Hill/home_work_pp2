import json

data = json

with open('sample_data.json', 'r') as file:
    data = json.load(file)

print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

for line in data["imdata"]:
    dn = line["l1PhysIf"]["attributes"]["dn"]
    desc = line["l1PhysIf"]["attributes"]["descr"]
    speed = line["l1PhysIf"]["attributes"]["speed"]
    mtu = line["l1PhysIf"]["attributes"]["mtu"]

    print(f"{dn:<50} {desc:<20} {speed:<9} {mtu}")

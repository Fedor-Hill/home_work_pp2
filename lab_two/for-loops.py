fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(6):
  print(x)  

print()
for x in range(2, 6):
  print(x)

print()
for x in range(2, 30, 3): #start, end, step
  print(x)

print()
for x in range(6):
  print(x)
else:
  print("Finally finished!")

print()
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

print()
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

for x in [0, 1, 2]:
  pass
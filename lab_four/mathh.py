import math

#
# 1 task
#
def degToRad() -> None:
    a = int(input("Radians: "))
    print(a * (math.pi / 180))


#
# 2 task
#
def trapezoid_area(height, base1, base2):
    return (base1 + base2) * height / 2


#
# 3 task
#
def polygon_area(num_sides, side_length):
    return int((num_sides * side_length**2) / (4 * math.tan(math.pi / num_sides)))


#
# 4 task
#
def parallelogram_area(base, height) -> float:
    return float(base * height)


# degToRad()

base = int(input())
h = int(input())
ans = parallelogram_area(base, h)

print(ans)

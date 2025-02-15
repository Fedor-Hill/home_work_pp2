#
# 1 task
#

def generate_squares(N: int):
    for i in range(N + 1):
        yield i**2


# res = generate_squares(10)

# for gens in res:
    # print(gens)

#
# 2 task
#
# n = int(input("n: "))

def evenNumb(n: int):
    answer = ""
    for i in range(0, n + 1):
        answer = answer + f"{i if i % 2 == 0 else ","}"
    yield answer
#
# res = evenNumb(n)
# for i in res:
#     print(i)

#
# 3 task
#
# n = int(input("n: "))

def numbByThreeAndFour(n: int):
    answer = ""
    for i in range(0, n + 1):
        answer = answer + f"{i if i % 12 == 0 else ","}"
    yield answer

# res = numbByThreeAndFour(n)
# for i in res:
#     print(i)

# 
# 4 task 
# 

def squares(a: int, b: int) -> None: 
    for i in range(a, b + 1):
        print(i**2)

squares(0, 10)

# 
# 5 task 
#
def toZero(n: int):
    while (n >= 0):
        yield n
        n-=1

res = toZero(12)
for i in res:
    print(i)

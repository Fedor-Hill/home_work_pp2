from itertools import permutations
import math
from random import randint


def gram_to_ounces(gram: float) -> float:  # 1 task
    return gram * 28.3495231


def faren_to_cels(F: float) -> float:  # 2 task
    C = (5 / 9) * (F - 32)
    return C


def solve(numheads: int, numlegs: int) -> None:  # 3 task

    rabbits = (numlegs - 2 * numheads) // 2
    chickens = numheads - rabbits

    print(f"We have {chickens} chicken and {rabbits} rabbits")


def is_prime(n: int):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def filter_prime(l: list[int]) -> list[int]:  # 4 task
    primes = []
    for n in l:
        if is_prime(n):
            primes.append(n)
    return primes


def print_permutations(s: str) -> None:  # 5 task
    perm = permutations(s)

    for p in perm:
        print("".join(p))


def reversed_words(s: str) -> str:  # 6 task

    return " ".join(s.split()[::-1])


def has_33(nums: list[int]) -> bool:  # 7 task

    for i in range(len(nums) - 1):
        if nums[i - 1] == 3 and nums[i] == 3:
            return True

    return False


def spy_game(nums: list[int]) -> bool:  # 8 task

    zero_count = 0

    for num in nums:
        if num == 0:
            zero_count += 1
        elif num == 7 and zero_count == 2:
            return True

    return False
 
def volume_of_sphere(r: float) -> float: # 9 task
    return (4/3) * math.pi * (r ** 3)

def unique_elements(l: list) -> list: # 10 task
    a = list()

    for original in l:
        if original not in a:
            a.append(original)

    return a

def is_palindrom(s: str) -> None: # 11 task

    if s == s[::-1]:
        print("it is palindrom")
    else:
        print("it is not palindrom")

def histogram(l: list[int]) -> None: # 12 task
    
    for h in l:
        print("*" * h)

def guess_the_number() -> None:
    name = input("Hello! What is your name?\n")
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")

    target = randint(1, 20)
    guesses = 0

    while True:
        num = int(input("Take a guess.\n"))
        guesses += 1


        if num < target:
            print("Your guess is too low.\n")

        elif num > target:
            print("Your guess is too high.\n")

        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break


def main() -> None:
    # solve(10, 28)

    # a = str(input("Input a string: "))
    # print( f"{a} -> {reversed_words(a)}")
    # print(spy_game([1, 2, 4, 0, 0, 7, 5]))
    
    # print(unique_elements([1, 1, 2, 3, 4, 4, 5, 4]))

    # histogram([4, 9, 7])

    guess_the_number()

    return None


if __name__ == "__main__":
    main()

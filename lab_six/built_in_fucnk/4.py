import time


def print_root_after_delay(number, delay_ms) -> None:
    delay_seconds = delay_ms / 1000.0
    time.sleep(delay_seconds)  
    result =  number**0.5  
    print(f"Square root of {number} after {delay_ms} miliseconds is {result}")

number = int(input("Input number: "))
ms = int(input("Input number: "))

print_root_after_delay(number, ms)

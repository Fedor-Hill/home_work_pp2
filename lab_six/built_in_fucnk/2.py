
def print_count_case_letters(input_string) -> None:
    upper_case_count = sum(1 for char in input_string if char.isupper()) 
    lower_case_count = sum(1 for char in input_string if char.islower()) 
    
    print(f"Upper count: {upper_case_count}")
    print(f"Lower count: {lower_case_count}")

s = input("Input string: ")
print_count_case_letters(s)

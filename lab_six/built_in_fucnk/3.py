
def is_palindrome(input_string):
    string = ''.join(char.lower() for char in input_string if char.isalnum())
    
    return string == string[::-1]

string = input("Input string: ")

if is_palindrome(string):
    print("Is palindrome")

else:
    print("Is not palindrome")

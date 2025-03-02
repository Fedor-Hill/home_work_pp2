import os


def make_clone(name: str):
    if os.path.exists(name) and os.path.isfile(name):
        with open(name, "r") as file:
            with open(f"copy_{name}", "w") as copy:
                copy.write(file.read())


input_file = input("Input file name to make copy: ")

make_clone(input_file)

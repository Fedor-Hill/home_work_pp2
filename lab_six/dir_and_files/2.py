import os

def check(path: str):
    if not os.path.exists(path):
        print("That Directory doen`t exists")
        return 

    if os.access(path, os.R_OK):
        print("That Directory is readable")
    else:
        print("That Directory is not readable")

    if os.access(path, os.W_OK):
        print("That Directory is writable")
    else:
        print("That Directory is not writable")

    if os.access(path, os.X_OK):
        print("That Directory is executive")
    else:
        print("That Directory is not executive")

path = input("Input path(enter for current directory): ")
if len(path) == 0:
    path = os.path.curdir

check(path)

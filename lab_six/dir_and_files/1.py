import os 

def list_directory(path: str):
    try:
        directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
        return directories
    except FileNotFoundError:
        print("The specified path does not exist.")
        return []


def list_files(path: str):
    try:
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        return files
    except FileNotFoundError:
        print("The specified path does not exist.")
        return []

def list_all(path: str):
    try:
        return os.listdir(path)
    except FileNotFoundError:
        print("The specified path does not exist.")
        return []

path = input("Input path(enter for current directory): ")
if len(path) == 0:
    path = os.path.curdir

test = list_all(path)
for d in test:
    print(d)

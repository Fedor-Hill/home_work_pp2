import os 

def check(path: str):
    if os.path.exists(path):
        print("Path exist")
        
        file_name = os.path.basename(path)
        print(f"File name: {file_name}")

        directory = os.path.dirname(path)
        print(f"directory portion: {directory}")
        return 
    
    print("Path not exist")

path = input("Input path(enter for current directory): ")
if len(path) == 0:
    path = os.path.curdir


check(path)

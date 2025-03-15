import os

def create_text_files():
    for i in range(26): 
        file_name = chr(65 + i) + '.txt'   
        with open(file_name, 'w') as file:
            file.write(f"{file_name}.txt")

def delete_create_files():
    for i in range(26): 
        file_name = chr(65 + i)   
        os.remove(f"{file_name}.txt")

# create_text_files()

delete_create_files()

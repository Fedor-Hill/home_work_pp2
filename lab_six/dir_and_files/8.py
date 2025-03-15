import os


def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):
            try:
                os.remove(file_path)
                print(f"The file '{file_path}' has been deleted.")
            except Exception as e:
                print(f"Error deleting file: {e}")
        else:
            print(f"The file '{file_path}' cannot be deleted.")
    else:
        print(f"The file '{file_path}' does not exist.")


input_file = input("Input file name (or path file) to delete: ")

delete_file(input_file)

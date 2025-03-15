def write_list_to_file(file_name, data_list):
    with open(file_name, "w") as file:
        for item in data_list:
            file.write(f"{item} ")


list_epta = ["a", "b", "c", "d"]

file_name = "letters"
write_list_to_file(file_name, list_epta)

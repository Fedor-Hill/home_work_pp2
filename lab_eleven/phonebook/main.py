from connect import connect as cc
from config import load_config
from instert_data import insert_to_phonebook
import delete_data
import update_data
import query_data 
import pattern_epta
import paginton

if __name__ == "__main__":
    config = load_config()
    cc(config)

    q = int(input("What do you want ?\n1 - insert data, 2 - delete data\n3 - update, 4 - query\n5 - pattern, 6 - instart many data\n7 - pagination: "))
    if q == 1:
        name = str(input("New name: "))
        phone = str(input("New phone number: "))
        if update_data.from_phonebook_by_name(name, phone, config):
            print("Name already use, update phone !")
        else:
            jid = insert_to_phonebook(name, phone, config)
            print("Succesful insert. Your id: " + str(jid))

    elif q == 2:
        print("Delete by name or phone ?")
        q = int(input("1 or 2: "))
        val = None
        if q == 1:
            val = str(input("Name: "))
            delete_data.from_phonebook_by_name(val, config)
        else: 
            val = str(input("Phone: "))
            delete_data.from_phonebook_by_phone(val, config)
            
    elif q == 3:
        print("Update by name or phone ?")
        q = int(input("1 or 2: "))
        if q == 1:
            name = str(input("Name: "))
            new_phone = str(input("New phone: "))

            update_data.from_phonebook_by_name(name, new_phone, config)
        else: 
            phone = str(input("Phone: "))
            new_name = str(input("New name: "))

            update_data.from_phonebook_by_phone(new_name, phone, config)
    elif q == 4:
        print("Query by all, name, phone or ASC name ?")
        q = int(input("[1, 2, 3, 4]: "))
        if q == 1:
            query_data.by_default(False, config)
        elif q == 2: 
            name = str(input("Name: "))
            query_data.by_name(name, config)
        elif q == 3: 
            phone = str(input("Phone: "))
            query_data.by_phone(phone, config)
        elif q == 4:
            query_data.by_default(True, config)

    elif q == 5:

        pattern = str(input("Enter search information (part of id or name or phone): "))
        results = pattern_epta.create_search_function(pattern, config)

        if results:
            print(results)
        else:
            print("Not found")
    elif q == 6: 
        print("Example: Ali 87779897 Atr 996876565 Lina 097875")
        datas = input("Inputs: ").split()

        if len(datas) % 2 != 0:
            print("Inccorect input. Not euqal number and name")
        else:
            for i in range(0, len(datas) - 1, 2):
                jid = insert_to_phonebook(datas[i], datas[i + 1], config)
                print("Succesful insert. Your id: " + str(jid))
    elif q == 7:
        limit = int(input("Limit: "))
        offset = int(input("Offset: "))

        paginton.love_jam(limit, offset, config)

    else:
        pass 

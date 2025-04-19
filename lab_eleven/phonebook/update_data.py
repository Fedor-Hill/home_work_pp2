import psycopg2
# from config import load_config

def from_phonebook_by_phone(name: str, phone: str, config):
    query = """UPDATE journal
             SET name = %s
             WHERE phone = %s;"""
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(query, (name, phone, ))
                # commit the changes to the database
                conn.commit()

                if cur.rowcount > 0:
                    print("Succesful update")
                else:
                    print(f"No records found with phone '{phone}'")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def from_phonebook_by_name(name: str, phone: str, config):
    query = """UPDATE journal
             SET phone = %s
             WHERE name = %s;"""
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(query, (phone, name, ))
                # commit the changes to the database
                conn.commit()

                if cur.rowcount > 0:
                    print("Succesful update")
                    return True
                else:
                    print(f"No records found with name '{name}'")
                    return False
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return False

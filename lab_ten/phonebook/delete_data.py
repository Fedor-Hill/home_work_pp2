import psycopg2
# from config import load_config

def from_phonebook_by_phone(phone: str, config):
    query = """DELETE FROM journal
             WHERE phone = %s;"""
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(query, (phone, ))
                # commit the changes to the database
                conn.commit()

                if cur.rowcount > 0:
                    print("Succesful delete")
                else:
                    print(f"No records found with phone '{phone}'")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def from_phonebook_by_name(name: str, config):
    query = """DELETE FROM journal
             WHERE name = %s;"""
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(query, (name, ))
                # commit the changes to the database
                conn.commit()

                if cur.rowcount > 0:
                    print("Succesful delete")
                else:
                    print(f"No records found with name '{name}'")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

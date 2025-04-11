import psycopg2
# from config import load_config

def insert_to_phonebook(name: str, phone: str, config):
    query = """INSERT INTO journal (name, phone)
             VALUES(%s, %s) RETURNING id;"""
    journal_id = None
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(query, (name, phone))

                # get the generated id back
                rows = cur.fetchone()
                if rows:
                    journal_id = rows[0]

                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return journal_id

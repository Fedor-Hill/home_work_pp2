import psycopg2
# from config import load_config

def by_default(asc: bool, config):
    query = "SELECT * FROM journal;"

    if asc:
        query = "SELECT * FROM journal ORDER BY name;"

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(query)

                for row in cur.fetchall():
                    print(row)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def by_name(name: str, config):
    query = """SELECT * FROM journal 
        WHERE name = %s;
    """

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(query, (name, ))

                for row in cur.fetchall():
                    print(row)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def by_phone(phone: str, config):
    query = """SELECT * FROM journal 
        WHERE phone = %s;
    """

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(query, (phone, ))

                for row in cur.fetchall():
                    print(row)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


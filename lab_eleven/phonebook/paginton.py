import psycopg2
# from config import load_config

def love_jam(limit: int, offset: int, config):
    query = """
        SELECT id, name, phone
        FROM journal
        ORDER BY id
        LIMIT %s OFFSET %s;
        """
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(query, (limit, offset, ))
                records = cur.fetchall()

                for epta in records:
                    print(epta)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

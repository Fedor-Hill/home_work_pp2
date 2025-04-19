import psycopg2

def create_search_function(pattern: str, config):
    query = """
        SELECT name, phone
        FROM "journal"
        WHERE name ILIKE %s OR phone ILIKE %s;
        """
    try:
        with psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                fpattern = f"%{pattern}%"
                cur.execute(query, (fpattern, fpattern, ))
                rows = cur.fetchall()

                return rows
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# def search_by_pattern(pattern, config):
#     try:
#         with psycopg2.connect(**config) as conn:
#             with  conn.cursor() as cur:
#
#                 cur.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
#                 rows = cur.fetchall()
#                 return rows
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)

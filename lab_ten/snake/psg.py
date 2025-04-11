import psycopg2
import data

class User:
    def __init__(self, user_id, name, direction, score, level, pos, speed):
        self.id = user_id
        self.name = name
        self.saved_direction = direction
        self.score = score 
        self.level = level 
        self.position = pos
        self.speed = speed 

def connect(config):
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

config = data.load_config()

def start():
    config = data.load_config()
    connect(config)

def get_user(name: str):
    query = """
        SELECT us.score, us.level, us.speed, u.id, u.position, u.direction
        FROM "User" u
        JOIN "userscore" us ON u.id = us.user_id
        WHERE u.username = %s;
        """

    user_id = None
    score, level = 0, 1
    saved_direction = None
    speed = 10
    current_position = []

    user = User(None, None, None, score, level, None, speed)

    with  psycopg2.connect(**config) as conn:
        with  conn.cursor() as cur:
            # execute the INSERT statement
            cur.execute(query, (name, ))

            row = cur.fetchone()

            if row:
                print(row)
                score, level, speed, user_id, current_position, saved_direction = row
                user.user_id = user_id
                user.name = name 
                user.position = current_position 
                user.saved_direction = saved_direction
                user.level = level if level != None else 1 
                user.score = score if score != None else 0 
                user.speed = speed if speed != None else 10

            else:
                query = """ INSERT INTO "User" (username) VALUES(%s) RETURNING id; """
                cur.execute(query, (name, ))
                user_id = cur.fetchall()[0]
                query = """ INSERT INTO "userscore" (user_id, score, level) VALUES(%s, %s, %s); """
                cur.execute(query, (user_id, 0, 0, ))

                user.user_id = user_id
                user.name = name

    return user

def save_data(user):
    query = """UPDATE "userscore" 
             SET score = %s, level = %s, speed = %s
             WHERE user_id = %s;"""

    with  psycopg2.connect(**config) as conn:
        with  conn.cursor() as cur:
            # execute the INSERT statement
            cur.execute(query, (user.score, user.level, user.speed, user.user_id, ))

    query = """UPDATE "User"
             SET position = %s, direction = %s
             WHERE "id" = %s;"""

    with  psycopg2.connect(**config) as conn:
        with  conn.cursor() as cur:
            # execute the INSERT statement
            cur.execute(query, (user.position, user.saved_direction, user.user_id, ))

    print("SAVE DATA COMPLETE")
    print(user.position)

movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"},
]

def more_than_five_point_five() -> None: 

    for movie in movies:
        if movie.get("imdb", 0) > 5.5:
            print(movie.get("name"))
            break

def list_more_than_five_point_five() -> list:
    a = list()

    for movie in movies:
        if movie.get("imdb", 0) > 5.5:
            
            a.append(movie)

    return a

def list_from_category(cat: str) -> list:
    a = list()

    for movie in movies:
        if movie.get("category")== cat:
            a.append(movie)

    return a

def average_imdb_scrore() -> None:

    ave = 0
    count = 0
    for movie in movies:
        num = movie.get("imdb", -1)

        if num != -1:
            ave += num
            count += 1

    print(f"Average score of list: {ave / count}")

def average_imdb_scrore_with_category(cat: str) -> None:

    ave = 0
    count = 0
    for movie in movies:
        if movie.get("category")== cat:
            num = movie.get("imdb", -1)

            if num != -1:
                ave += num
                count += 1

    print(f"Average score of list with category {cat}: {ave / count}")



def main():
    more_than_five_point_five()

    print(list_more_than_five_point_five())
    print(list_from_category("Romance"))
    average_imdb_scrore()
    average_imdb_scrore_with_category("Romance")

if __name__ == "__main__":
    main()

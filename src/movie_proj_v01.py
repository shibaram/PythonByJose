movies_list_master = [
    {"movie_name": "Black Panther",
     "director": "j ross",
     "release_year": 2007,
     "genre": ("action", "sci-fi"),
     "actors": ("Chadwick Boseman", "Lupita Nyong")
     },
    {"movie_name": "Inception",
     "director": "Christopher",
     "release_year": 2010,
     "genre": ("action", "sci-fi"),
     "actors": ("Leonardo  Dicaprio", "Joseph")},
    {"movie_name": "Avenger Endgame",
     "director": "Joe Ross",
     "release_year": 2019,
     "genre": ("action", "sci-fi"),
     "actors": ("Chrish hamsscotch", "Scarlett Johnson", "Robert downy jr")},
    {"movie_name": "DDLJ",
     "director": "Aditya Chopra",
     "release_year": 1995,
     "genre": ("Drama", "Romance"),
     "actors": ("Sharukh", "Kajol")}
]


def get_all_cur_movies_from_masterlist():
    return f"Movies in the master list count was {len(movies_list_master)} adding new movie:\n{movies_list_master}"


print("Before: ", get_all_cur_movies_from_masterlist())


def input_movie_details_byconsole():
    movie_name = input("Movie Name: ")
    director_name = input("Director Name: ")
    release_year = int(input("Release Year: "))
    genre = input("genre (separated by comma): ")
    actors = input("Actors Names (separated by comma): ")

    movie_by_user = {"movie_name": movie_name,
                     "director": director_name,
                     "release_year": release_year,
                     "genre": genre,
                     "actors": actors}

    return movie_by_user


def add_movie_to_masterlist(movie_by_console):
    movies_list_master.append(movie_by_console)


# below are testing section
movie_dict = input_movie_details_byconsole()
add_movie_to_masterlist(movie_dict)
print("After: ", get_all_cur_movies_from_masterlist())

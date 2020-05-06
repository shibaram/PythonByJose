from movie_proj_v01.movie import Movie
from movie_proj_v01.moviesdb import MoviesDB


def input_movie_details():
    movie_name = input("Movie Name: ")
    director_name = input("Director Name: ")
    release_year = int(input("Release Year: "))
    genre = input("genre (separated by comma): ")

    movie_by_user = Movie(movie_name, director_name, release_year, genre)

    return movie_by_user


mdb = MoviesDB()

"""
DDLJ = Movie("DDLJ", "Sharukh", 1994, "Drama")
singham = Movie("Singham", "Rohit", 2012, "Drama, Action")

mdb.add_new_movie(DDLJ)
mdb.add_new_movie(singham)
"""
user_movie = input_movie_details()
# mdb.add_new_movie(user_movie)
# mdb.show_movies()
# user_search = input("Search here: ")

# print("Your search movie details is:\n", mdb.find_movie(user_search))

mdb.add_movie_db_text_file(user_movie)

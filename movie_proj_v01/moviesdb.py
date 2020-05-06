class MoviesDB:
    def __init__(self):
        self.movies_db = []

    def add_new_movie(self, movie_name):
        self.movies_db.append(movie_name)

    def show_movies(self):
        print(f" {len(self.movies_db)} number movies are stored in db and below are details:.")
        for movie in self.movies_db:
            print(movie)
            print()

    def find_movie(self, user_search):
        for mov in self.movies_db:
            if mov.movie_name.lower() == user_search.lower():
                return mov

    def add_movie_db_text_file(self, new_movie1):
        w_file = open("movie_proj_v01/movies_db.txt", "a")
        movie_n = f"{new_movie1.movie_name},{new_movie1.director}, {new_movie1.year}, {new_movie1.genre}"
        w_file.write(movie_n)
        w_file.close()

class Movie:

    def __init__(self, movie_name, director, year, genre):
        self.movie_name = movie_name
        self.director = director
        self.year = year
        self.genre = genre

    def __str__(self):
        return f" Movie: {self.movie_name} \n Director: {self.director} \n Year: {self.year} \n Genre: {self.genre} "




class MovieSelector():
    def __init__(self):
        pass

    def get_movies_matching_genre(self, movies, genre):
        matching_movies = []
        for movie in movies:
            for movie_genre in movie.genre:
                if movie_genre == genre:
                    matching_movies.append(movie)
                    break
        return matching_movies

    def get_movies_matching_search(self, movies, search):
            matching_movies = []
            for movie in movies:
                matching_genre = False
                for genre in movie.genre:
                    if search.lower() == genre.lower():
                        matching_genre = True
                        break
                
                if ((search.lower() in movie.title.lower()) or matching_genre):
                    print("Append")
                    matching_movies.append(movie)

            return matching_movies

    def get_movie_matching_title(self, movies, title):
        for movie in movies:
            if movie.title == title:
                return movie
    
    def select(self, movies, title=None, genre=None, search=None):
        if title:
            return self.get_movie_matching_title(movies, title)
        if genre:
            movies = self.get_movies_matching_genre(movies, genre) 
        if search:
            movies = self.get_movies_matching_search(movies, search) 
        return movies
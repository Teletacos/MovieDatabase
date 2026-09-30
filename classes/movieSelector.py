class MovieSelector():
    def __init__(self):
        pass

    def get_movies_matching_genres(self, movies, genres):
        matching_movies = []
        for movie in movies:
            matching = True
            for genre in genres:
                if not genre in movie.genre:
                    matching = False
            if matching: matching_movies.append(movie)
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
                    matching_movies.append(movie)

            return matching_movies

    def get_movie_matching_title(self, movies, title):
        for movie in movies:
            if movie.title == title:
                return movie
    
    def select(self, movies, title=None, genres=None, search=None):
        if title:
            return self.get_movie_matching_title(movies, title)
        if genres:
            movies = self.get_movies_matching_genres(movies, genres) 
        if search:
            movies = self.get_movies_matching_search(movies, search) 
        return movies

    def sort(self, movies, sort_mode):
        try:
            key_name, direction = sort_mode.lower().split(" ")
            reverse = True
            if direction == "ascending": reverse = False
            return sorted(movies, key=lambda item: getattr(item, key_name), reverse=reverse)
        except:
            return movies

    def get_all_genres(self, movies):
        genres = set()
        for movie in movies: 
            for genre in movie.genre:
                genres.add(genre)
        genres = list(genres)
        genres.sort()
        return genres
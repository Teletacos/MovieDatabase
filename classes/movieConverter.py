from classes.movie import Movie

class MovieConverter():
    movie_properties = ["title", "director", "cast", "year", "genre", "rating"]

    def __init__(self, fileHandler):
        self.fileHandler = fileHandler

    def dict_to_movie(self, dictionary):
        movie = Movie()
        for property in MovieConverter.movie_properties:
            setattr(movie, property, dictionary[property])
        return movie

    def movie_to_dict(self, movie):
        dictionary = {}
        for property in MovieConverter.movie_properties:
            dictionary[property] = getattr(movie, property)
        return dictionary
            
    def dicts_list_to_movies_list(self, dicts_list):
        movie_list = []
        for dictionary in dicts_list:
            movie_list.append(self.dict_to_movie(dictionary))
        return movie_list

    def movies_list_to_dicts_list(self, movies_list):
        dicts_list = []
        for movie in movies_list:
            dicts_list.append(self.movie_to_dict(movie))
        return dicts_list

    def load_movies(self):
        return self.dicts_list_to_movies_list(self.fileHandler.load_data())

    def save_movies(self, movies):
        self.fileHandler.save_data(self.movies_list_to_dicts_list(movies))

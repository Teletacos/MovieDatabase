from flask import Flask, render_template, request
from classes.JSONHandler import JSONHandler
from classes.movieConverter import MovieConverter
from classes.movieSelector import MovieSelector
from classes.movie import Movie

def main():
    movieJsonHandler = JSONHandler("static/database/movies.json")
    movieConverter = MovieConverter(movieJsonHandler)
    movieSelector = MovieSelector()

    app = Flask(__name__)

    @app.route("/")
    def index():
        movies = movieConverter.load_movies()
        genres = movieSelector.get_all_genres(movies)
        selected_search = request.args.get("search") or ""
        selected_sort = request.args.get("sort-mode")
        selected_genres = []
        for genre, value in request.args.items():
            if value == "on":
                selected_genres.append(genre)
        selected_movies = movieSelector.select(movies, search=selected_search, genres=selected_genres)
        selected_movies = movieSelector.sort(selected_movies, selected_sort)
        return render_template(
            "index.html", 
            movies=selected_movies, 
            genres=genres, 
            sort_modes=["Title Ascending", "Title Descending", "Year Ascending", "Year Descending", "Rating Ascending", "Rating Descending"], 
            selected_search=selected_search, 
            selected_genres=selected_genres, 
            selected_sort=selected_sort
        )

    @app.route("/movie/<title>")
    def movie(title):
        movies = movieConverter.load_movies()
        movie = movieSelector.select(movies, title=title)
        return render_template("movie.html", movie=movie)

    app.run(port=80)

main()
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
        search = request.args.get("search")
        movies = movieSelector.select(movies, search=search)
        return render_template("index.html", current_view="Explore", movies=movies)

    @app.route("/movie/<title>")
    def movie(title):
        movies = movieConverter.load_movies()
        movie = movieSelector.select(movies, title=title)
        return render_template("movie.html", movie=movie)

    @app.route("/genre/<genre>")
    def genre(genre):
        movies = movieConverter.load_movies()
        search = request.args.get("search")
        movies = movieSelector.select(movies, genre=genre, search=search)
        return render_template("index.html", current_view=genre, movies=movies)

    app.run(port=80)

main()
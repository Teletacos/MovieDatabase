class Movie():
    def __init__(self):
        self.title = "title"
        self.director = "director"
        self.cast = ["cast"]
        self.year = 0
        self.genre = "genre"

    @property
    def image_path(self):
        path = ""
        name_parts = self.title.lower().replace(":", "").split(" ")
        if len(name_parts) > 1 and name_parts[0] == "the":
            path = name_parts[0] + "_" + name_parts[1]
        elif len(name_parts) > 1 and name_parts[0] == "cars":
            path = name_parts[0] + name_parts[1]
        else:
            path = name_parts[0]
        path = f"images/movies/{path}.jpg"
        return path
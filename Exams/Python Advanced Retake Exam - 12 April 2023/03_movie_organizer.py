def movie_organizer(*args):
    movies = {}

    for movie in args:
        movie_name = movie[0]
        movie_genre = movie[1]

        if movie_genre not in movies:
            movies[movie_genre] = []
        movies[movie_genre].append(movie_name)

    sorted_movies = sorted(movies.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ""

    for k, v in sorted_movies:
        result += f"{k} - {len(v)}\n"
        for name in sorted(v):
            result += f"* {name}\n"

    return result

print(movie_organizer(
    ("The Matrix", "Sci-fi")))

print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))

print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))

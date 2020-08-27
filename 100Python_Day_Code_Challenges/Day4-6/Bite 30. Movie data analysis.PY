import csv
from collections import defaultdict, namedtuple


#MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')

file = open("D:\CyberSecuritY\Programming\Python\\100Python_Day_Code_Challenges\Day4-6\Movies.csv", encoding="utf-8")
csv_reader = csv.DictReader(file)

def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    directors = defaultdict(list)
    for line in csv_reader:
        try:
            director = line['director_name']
            movie = line['movie_title'].replace('\xa0', '')
            year = int(line['title_year'])
            score = float(line['imdb_score'])
        except ValueError:
            continue
        if year and year < MIN_YEAR:
            continue

        directors[director].append(movie)

    print(directors)
get_movies_by_director()
director_movies = get_movies_by_director()
def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    ratings = [m.score for m in movies]
    mean = sum(ratings) / max(1, len(ratings))
    return round(mean, 1)
#calc_mean_score(director_movies['Sergio Leone'])
def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    ret = {director: calc_mean_score(movies)
            for director, movies in directors.items()
            if len(movies) >= MIN_MOVIES}
    return sorted(ret.items(), key=lambda x: x[1], reverse=True)

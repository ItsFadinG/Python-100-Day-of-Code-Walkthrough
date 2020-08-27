import csv
import collections
Movie = collections.namedtuple('Movie', 'title year score')
directors = collections.defaultdict(list)
with open('D:\\CyberSecuritY\\Programming\\Python\\100Python_Day_Code_Challenges\\Day4-6\\Movies.csv', encoding='utf-8') as f:
    for line in csv.DictReader(f):
        try:
            director = line['director_name']
            movie = line['movie_title'].replace('\xa0', '')
            year = int(line['title_year'])
            score = float(line['imdb_score'])
        except ValueError:
            continue
        m = Movie(title=movie, year=year, score=score)
        directors[director].append(m)

print(directors)

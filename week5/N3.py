films = [
    {"название": "Фильм 1", "рейтинг": 8.5, "жанр": "комедия", "год выпуска": 2010},
    {"название": "Фильм 2", "рейтинг": 7.9, "жанр": "драма", "год выпуска": 2015},
    {"название": "Фильм 3", "рейтинг": 9.2, "жанр": "фантастика", "год выпуска": 2005},
    {"название": "Фильм 4", "рейтинг": 8.1, "жанр": "комедия", "год выпуска": 2010},
    {"название": "Фильм 5", "рейтинг": 7.5, "жанр": "драма", "год выпуска": 2000}
]


def sort_films(film):
    return (film["рейтинг"], film["жанр"], film["год выпуска"])


sorted_films = sorted(films, key=sort_films)

for film in sorted_films:
    print(film)
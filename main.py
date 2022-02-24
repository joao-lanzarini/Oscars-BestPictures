from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

# OSCARS BEST PICTURES WINNERS
w_url = "https://www.imdb.com/list/ls009480135/"
w_request = requests.get(w_url)
w_page = bs(w_request.content, 'html.parser')

w_title_divs = w_page.find_all(class_='lister-item-header')
w_age_divs = w_page.find_all("span", class_="certificate")
w_time_divs = w_page.find_all("span", class_="runtime")
w_genre_divs = w_page.find_all("span", class_="genre")
w_rating_divs = w_page.find_all("span", class_="ipl-rating-star__rating")

# OSCARS BEST PICTURES NOMINEES
n_url = "https://www.imdb.com/list/ls009487211/"
n_request = requests.get(n_url)
n_page = bs(n_request.content, 'html.parser')

n_title_divs = n_page.find_all(class_='lister-item-header')
n_age_divs = n_page.find_all("span", class_="certificate")
n_time_divs = n_page.find_all("span", class_="runtime")
n_genre_divs = n_page.find_all("span", class_="genre")
n_rating_divs = w_page.find_all("span", class_="ipl-rating-star__rating")

# CREATING DATAFRAME
winner_movies = {
    'title': [],
    'year': [],
    'rating': [],
    'time': [],
    'genre': [],
    'age': []
}

nominated_movies = {
    'title': [],
    'year': [],
    'rating': [],
    'time': [],
    'genre': [],
    'age': []
}

# HANDLING WINNERS DATA
for i in w_title_divs:
    c=0
    for a in i:
        if c == 3:
            winner_movies['title'].append(a.get_text())

        elif c == 5:
            winner_movies['year'].append(a.get_text())

        c += 1

for i in w_time_divs:
    winner_movies['time'].append(i.get_text())


c=0
for i in w_rating_divs:
    if c%23 == 0:
        winner_movies['rating'].append(i.get_text())
    c+=1


for i in w_genre_divs:
    gen = i.get_text()
    winner_movies['genre'].append(gen.rstrip().replace('\n', ''))

for i in w_age_divs:
    winner_movies['age'].append(i.get_text())


# HANDLING NOMINEES DATA
for i in n_title_divs:
    c=0
    for a in i:
        if c == 3:
            nominated_movies['title'].append(a.get_text())

        elif c == 5:
            nominated_movies['year'].append(a.get_text())

        c += 1

for i in n_time_divs:
    nominated_movies['time'].append(i.get_text())


c=0
for i in n_rating_divs:
    if c%23 == 0:
        nominated_movies['rating'].append(i.get_text())
    c+=1


for i in n_genre_divs:
    gen = i.get_text()
    nominated_movies['genre'].append(gen.rstrip().replace('\n', ''))

for i in n_age_divs:
    nominated_movies['age'].append(i.get_text())






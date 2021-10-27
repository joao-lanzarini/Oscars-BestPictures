from bs4 import BeautifulSoup as bs
import requests


# OSCARS BEST PICTURES WINNERS
w_url = "https://www.imdb.com/list/ls009480135/"
w_request = requests.get(w_url)
w_page = bs(w_request.content, 'html.parser')

# OSCARS BEST PICTURES NOMINEES
n_url = "https://www.imdb.com/list/ls009487211/"
n_request = requests.get(n_url)
n_page = bs(n_request.content, 'html.parser')

n_title_divs = n_page.find_all(class_='lister-item-header')
w_title_divs = w_page.find_all(class_='lister-item-header')

title=[]
year=[]

for i in w_title_divs[0:8]:
    c=0
    for a in i:
        if c == 3:
            title.append(a.get_text())
        elif c == 5:
            year.append(a.get_text())

        c+=1

print(title)
print(year)


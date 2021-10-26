from bs4 import BeautifulSoup as bs
import requests

url = "https://www.imdb.com/list/ls009487211/"
request = requests.get(url)
html_page = bs(request.content, 'html.parser')

title_divs = html_page.find_all(class_='lister-item-header')

title=[]
year=[]

for i in title_divs[0:8]:
    c=0
    for a in i:
        if c == 3:
            title.append(a.get_text())
        elif c == 5:
            year.append(a.get_text())

        c+=1

print(title)
print(year)


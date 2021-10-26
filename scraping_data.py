from bs4 import BeautifulSoup as bs
import requests

url = "https://www.imdb.com/list/ls009487211/"
request = requests.get(url)
html_page = bs(request.content, 'html.parser')

title_divs = html_page.find_all(class_='lister-item-header')
years = html_page.find_all(class_='lister-item-year text-muted unbold')

for i in title_divs[3]:
    print(i)

print(years[17].get_text())


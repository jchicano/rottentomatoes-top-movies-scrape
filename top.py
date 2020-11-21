import re
import requests
from bs4 import BeautifulSoup

year = input('Enter the year: ')

req = requests.get('https://www.rottentomatoes.com/top/bestofrt/?year=' + year)
soup = BeautifulSoup(req.text, 'lxml')

table = soup.select('html body.body div.body_main.container div#main_container.container div.col-left-center.col-full-xs section#top_movies_main.panel.panel-rt.panel-box div.panel-body.content_body.allow-overflow table.table')[0]

array_tmp = []
for tr in table.findAll('tr'):
    array_tmp += tr.get_text().split('\n')

# Remove empty items in list
sans_whitespace = [s for s in array_tmp if s.strip()]

print(len(sans_whitespace))

array = [0] * 404
for index,item in enumerate(sans_whitespace):
    sans_whitespace[index] = re.sub(' +', ' ', item) # Remove multiple whitespaces
    sans_whitespace[index] = ' '.join(sans_whitespace[index].split()) # Remove icon next to rating
    array[index] = sans_whitespace[index]

# Pretty print array
counter = 1
for i in range(len(array)):
    if counter == 4:
        print(array[i], end='\n')
        counter = 0
    else:
        print(array[i], end='\t')
    counter += 1


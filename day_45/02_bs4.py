import requests
from bs4 import BeautifulSoup

contents = requests.get(url='https://news.ycombinator.com/news').text
soup = BeautifulSoup(markup=contents, features='html.parser')
titles = [x.text for x in soup.select(selector='.titleline > a')]
links = [x.get('href') for x in soup.select(selector='.titleline > a')]
scores = [int(x.text.split()[0]) for x in soup.select(selector='.score')]
max_score_index = scores.index(max(scores)) - 1
max_score_title = titles[max_score_index]
max_score_link = links[max_score_index]
max_score = scores[max_score_index]
print(max_score_title)
print(max_score_link)
print(max_score)

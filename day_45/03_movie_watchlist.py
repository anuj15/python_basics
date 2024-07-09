import requests
from bs4 import BeautifulSoup

URL_1 = "https://web.archive.org/web/20200518073855/"
URL_2 = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL_2).text
soup = BeautifulSoup(response, 'html.parser')
all_movies = [x.text for x in soup.find_all(name='h3', class_='listicleItem_listicle-item__title__BfenH')]
movies = all_movies[::-1]
with open(file='movie.txt', mode='w', encoding='utf-8') as f:
    for movie in movies:
        f.write(f'{movie}\n')

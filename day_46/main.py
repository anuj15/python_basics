import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

user_date = input('Which year do you want to travel to? Type the date in this format: YYYY-MM-DD: ')
year = user_date.split('-')[0]
url = f'https://www.billboard.com/charts/hot-100/{user_date}/'
response = requests.get(url=url).text
soup = BeautifulSoup(markup=response, features='html.parser')
song_names = [x.text.strip() for x in soup.select(selector='li > h3#title-of-a-story')]

cid = '449d2a6ce0cb487381cd3d3160515c4b'
secret = '71eb5045fa8a440ebe83ca154df77722'
uri = 'http://example.com'
scope = 'playlist-modify-private'
file = 'token.txt'
user = 'Anuj'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, redirect_uri=uri, client_id=cid, client_secret=secret,
                                               show_dialog=True, cache_path=file, username=user))
user_id = sp.current_user()["id"]
song_uris = []
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        continue
playlist = sp.user_playlist_create(user=user_id, name=f'{user_date} Billboard 100', public=False)
sp.playlist_add_items(playlist['id'], song_uris)

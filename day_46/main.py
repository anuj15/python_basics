# import requests
import urllib3
# from bs4 import BeautifulSoup
#
urllib3.disable_warnings()
#
# user_date = input('Which year do you want to travel to? Type the date in this format: YYYY-MM-DD: ')
# my_date = '2000-08-12'
# url = f'https://www.billboard.com/charts/hot-100/{my_date}/'
# response = requests.get(url=url, verify=False).text
# soup = BeautifulSoup(markup=response, features='html.parser')
# titles = [x.text.strip() for x in soup.select(selector='li > h3#title-of-a-story')]
# print(titles)
#
# data = ['Incomplete', 'Bent', "It's Gonna Be Me", "Jumpin', Jumpin'", 'Try Again', 'I Wanna Know',
#         'Everything You Want', 'Absolutely (Story Of A Girl)', 'Higher', "Doesn't Really Matter", 'I Need You',
#         'No More', "He Wasn't Man Enough", "Let's Get Married", 'Back Here', 'There You Go',
#         '(Hot S**t) Country Grammar', 'Kryptonite', 'Desert Rose', 'Wifey', "I Think I'm In Love With You",
#         'You Sang To Me', 'Breathe', 'I Wanna Be With You', 'Wonderful', "What'Chu Like", 'The Next Episode',
#         'Be With You', 'I Turn To You', "That's The Way", 'Separated', 'I Will Love Again', 'I Hope You Dance',
#         'What About Now', "Big Pimpin'", 'Smooth', 'Purest Of Pain (A Puro Dolor)', "Prayin' For Daylight",
#         'It Must Be Love', 'I Try', 'Music', 'Where I Wanna Be', 'Faded', 'One Voice', 'Amazed', 'Dance Tonight',
#         'Come On Over Baby (All I Want Is You)', 'Whatever', 'The Real Slim Shady', 'Flowers On The Wall',
#         'Just Be A Man About It', 'Simple Kind Of Life', 'Yes!', 'Could I Have This Kiss Forever', 'The Light',
#         'Swear It Again', "Callin' Me", 'Taking You Home', 'I Will...But', "I'll Be", 'Lucky', 'What You Want',
#         'Change Your Mind', "It's My Life", 'No Matter What They Say', "Don't Think I'm Not", 'Your Everything',
#         "You'll Always Be Loved By Me", 'Last Resort', 'Cold Day In July', 'As We Lay', 'Californication',
#         'Crash And Burn', 'Broadway', 'Treat Her Like A Lady', 'Who Let The Dogs Out', 'Oops!...I Did It Again',
#         'Country Comes To Town', 'Better Off Alone', 'When You Need My Love', "It's Always Somethin'", 'Dance With Me',
#         "Let's Make Love", 'West Side Story', 'Most Girls', 'With Arms Wide Open', 'Sour Girl', 'I Disappear',
#         'I Think God Can Explain', 'The One', 'Same Script, Different Cast', "Don't Call Me Baby",
#         'Some Things Never Change', 'The Chain Of Love', 'Got It All', 'Wobble Wobble', 'Shake Ya Ass', 'Hey Papi',
#         'Imagine That', 'Ta Da']

import spotipy

id = '449d2a6ce0cb487381cd3d3160515c4b'
secret = '71eb5045fa8a440ebe83ca154df77722'
uri = 'http://example.com'

x = spotipy.oauth2.SpotifyOAuth(client_id=id, client_secret=secret, redirect_uri=uri, scope= 'playlist-modify-private')
token = x.get_access_token()
print(token)

OAUTH_TOKEN_URL = 'https://accounts.spotify.com/api/token'
OAUTH_AUTHORIZE_URL = 'https://accounts.spotify.com/authorize'

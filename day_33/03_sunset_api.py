from datetime import datetime as dt

import requests

my_lat = 51.507351
my_long = -0.127758

parameters = {
    'lat': my_lat,
    'lng': my_long,
    'formatted': 0,
}
response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
sunset = data['results']['sunset'].split('T')[1].split(':')[0]
sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
print(sunset)
print(sunrise)
now = dt.now()
print(now.hour)

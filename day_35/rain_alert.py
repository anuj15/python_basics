import requests

from twilio_messages import *

OWM_API_KEY = '5c0be521628ced88241158b7b7122011'
OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'
params = {
    'lat': 25,
    'lon': 92,
    'appid': OWM_API_KEY,
    'cnt': 4,
}
response = requests.get(url=OWM_ENDPOINT, params=params)
response.raise_for_status()
data = response.json()['list']
weather_codes = [x['weather'][0]['id'] for x in data]
for code in weather_codes:
    if code <= 500:
        sms('Bring an umbrella')
    else:
        whatsapp('Do not bring an umbrella')

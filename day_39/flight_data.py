import requests

API_KEY = 'TU9IzwVX5AS4R4qbWIPjc06mHrvHAGhc'
API_SECRET = 'sntS7BJ8No7zLUjD'


# Token: https://developers.amadeus.com/self-service/category/destination-experiences/api-doc/city-search/api-reference


def get_token():
    url = 'https://test.api.amadeus.com/v1/security/oauth2/token'
    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'grant_type': 'client_credentials',
        'client_id': API_KEY,
        'client_secret': API_SECRET,
    }
    response = requests.post(url=url, data=data, headers=header)
    return response.json()['access_token']


def get_iata_code(country, city):
    endpoint = 'https://test.api.amadeus.com/v1/reference-data/locations/cities'
    parameters = {
        'countryCode': country,
        'keyword': city,
    }
    headers = {
        'Authorization': f'Bearer {get_token()}',
    }
    response = requests.get(url=endpoint, params=parameters, headers=headers)
    return response.json()['data'][0]['iataCode']

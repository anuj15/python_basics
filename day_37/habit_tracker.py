from datetime import datetime as dt

import requests

PIXELA_BASE_URL = 'https://pixe.la'
USER_ENDPOINT = f'{PIXELA_BASE_URL}/v1/users'
TOKEN = 'anuj1234'
USERNAME = 'anuj1234'
GRAPH_ENDPOINT = f'{USER_ENDPOINT}/{USERNAME}/graphs'
GRAPH_ID = 'graph1'
PIXEL_ENDPOINT = f'{GRAPH_ENDPOINT}/{GRAPH_ID}'
RANDOM_DAY = dt(year=2024, month=6, day=19).strftime('%Y%m%d')
UPDATE_PIXEL_ENDPOINT = f'{PIXEL_ENDPOINT}/{RANDOM_DAY}'
HEADERS = {
    'X-USER-TOKEN': TOKEN,
}


def create_user():
    parameters = {
        'token': TOKEN,
        'username': USERNAME,
        'agreeTermsOfService': 'yes',
        'notMinor': 'yes',
    }
    response = requests.post(url=USER_ENDPOINT, json=parameters)
    print(response.text)


def create_graph():
    parameters = {
        'id': GRAPH_ID,
        'name': 'graph1',
        'unit': 'Km',
        'type': 'float',
        'color': 'ajisai',
    }
    response = requests.post(url=GRAPH_ENDPOINT, json=parameters, headers=HEADERS)
    print(response.text)


def create_pixel():
    parameters = {
        'date': RANDOM_DAY,
        'quantity': '5',
    }
    response = requests.post(url=PIXEL_ENDPOINT, json=parameters, headers=HEADERS)
    print(response.text)


def update_pixel():
    parameters = {
        'quantity': '10',
    }
    response = requests.put(url=UPDATE_PIXEL_ENDPOINT, json=parameters, headers=HEADERS)
    print(response.text)


def delete_pixel():
    response = requests.delete(url=UPDATE_PIXEL_ENDPOINT, headers=HEADERS)
    print(response.text)


delete_pixel()

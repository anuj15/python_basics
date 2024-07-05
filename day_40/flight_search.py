from datetime import date, timedelta

from flight_data import *

urllib3.disable_warnings()
SOURCE_IATA = 'DEL'
END_DATE = date.today() + timedelta(days=180)
response = ''


def flight_search(destination_iata, non_stop='true'):
    global response
    endpoint = 'https://test.api.amadeus.com/v2/shopping/flight-offers'
    headers = {
        'Authorization': f'Bearer {get_token()}',
    }
    for day in range(1, 3):
        to_day = date.today() + timedelta(days=day)
        params = {
            'originLocationCode': SOURCE_IATA,
            'destinationLocationCode': destination_iata,
            'departureDate': to_day,
            'adults': 1,
            'currencyCode': 'INR',
            'nonStop': non_stop,
        }
        response = requests.get(url=endpoint, params=params, headers=headers, verify=False).json()
        if response['meta'].get('count') == 0:
            response = flight_search(destination_iata, 'false')
        return response


def get_stops():
    return len(response['data'][0]['itineraries'][0]['segments']) - 1


def get_min_flight_price(destination_iata):
    x = flight_search(destination_iata)
    prices = [{x['price']['total']: x['lastTicketingDate'] for x in x['data']}]
    return {min(x.keys()): x[min(x.keys())] for x in prices}

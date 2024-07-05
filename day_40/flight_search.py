from datetime import date, timedelta

from flight_data import *

urllib3.disable_warnings()
SOURCE_IATA = 'DEL'
END_DATE = date.today() + timedelta(days=180)


def get_min_flight_price(destination_iata):
    endpoint = 'https://test.api.amadeus.com/v2/shopping/flight-offers'
    headers = {
        'Authorization': f'Bearer {get_token()}',
    }
    prices = []
    for day in range(1, 3):
        to_day = date.today() + timedelta(days=day)
        params = {
            'originLocationCode': SOURCE_IATA,
            'destinationLocationCode': destination_iata,
            'departureDate': to_day,
            'adults': 1,
            'currencyCode': 'INR',
        }
        response = requests.get(url=endpoint, params=params, headers=headers, verify=False).json()['data']
        prices.append({x['price']['total']: x['lastTicketingDate'] for x in response})
    return {min(x.keys()): x[min(x.keys())] for x in prices}

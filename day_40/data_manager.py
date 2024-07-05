import requests

api_key = 'b0275f7af437836b333007208e74149d'
workbook = 'flightDeals'
sheet_1 = 'prices'
sheet_2 = 'users'


def get_cities():
    url = f'https://api.sheety.co/{api_key}/{workbook}/{sheet_1}'
    response = requests.get(url=url)
    return {x['country']: x['city'] for x in response.json()['prices']}


def compare_prices():
    data = []
    url = f'https://api.sheety.co/{api_key}/{workbook}/{sheet_1}'
    response = requests.get(url=url).json()['prices']
    for row in response:
        if float(row['myprice']) >= float(row['lowestprice']):
            data.append(row)
    return data


def set_iata_code(row, code):
    url = f'https://api.sheety.co/{api_key}/{workbook}/{sheet_1}/{row}'
    data = {
        'price': {
            'iatacode': code,
        }
    }
    response = requests.put(url=url, json=data)
    return response.status_code == 200


def set_lowest_price(row, price):
    url = f'https://api.sheety.co/{api_key}/{workbook}/{sheet_1}/{row}'
    data = {
        'price': {
            'lowestprice': price,
        }
    }
    response = requests.put(url=url, json=data)
    return response.status_code == 200


def set_lowest_price_date(row, date):
    url = f'https://api.sheety.co/{api_key}/{workbook}/{sheet_1}/{row}'
    data = {
        'price': {
            'date': date,
        }
    }
    response = requests.put(url=url, json=data)
    return response.status_code == 200


def set_user_data(data):
    url = f'https://api.sheety.co/{api_key}/{workbook}/{sheet_2}'
    data = {
        'user': {
            'firstName': data[0],
            'lastName': data[1],
            'email': data[2],
        }
    }
    response = requests.post(url=url, json=data)
    return response.status_code == 200


def get_user_data():
    url = f'https://api.sheety.co/{api_key}/{workbook}/{sheet_2}'
    response = requests.get(url=url).json()['users']
    return [x['email'] for x in response]

import requests

from twilio_messages import *

STOCK_API_KEY = 'YF6VHYEBRFFSG1ZK'
NEWS_API_KEY = '008c016a654a470090cae7c1532abc80'
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'
STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
STOCK = 'TSLA'
COMPANY_NAME = 'Tesla Inc'


def get_news():
    parameters = {
        'q': COMPANY_NAME,
        'apiKey': NEWS_API_KEY,
    }
    response = requests.get(url=NEWS_ENDPOINT, params=parameters)
    response.raise_for_status()
    return response.json()['articles'][:3]


def get_stock_price():
    parameters = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': STOCK,
        'apikey': STOCK_API_KEY,
    }
    response = requests.get(url=STOCK_ENDPOINT, params=parameters)
    response.raise_for_status()
    data = [v['4. close'] for (k, v) in response.json()['Time Series (Daily)'].items()][:2]
    y_close_price = float(data[0])
    dby_close_price = float(data[1])
    return round((dby_close_price - y_close_price) * 100 / dby_close_price)


value = get_stock_price()

if value > 0:
    symbol = '🔺'
else:
    symbol = '🔻'
for news in get_news():
    msg = f'{STOCK}: {symbol}{value}%\nHeadline: {news["title"]}\nBrief: {news["description"]}'
    sms(msg)

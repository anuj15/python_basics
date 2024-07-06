from data_manager import *
from flight_search import *
from notification_manager import *
from users import *

msg = ''
stops = 0
row = 2
for country, city in get_cities().items():
    iata_code = get_iata_code(country, city)
    set_iata_code(row, iata_code)
    min_price = get_min_flight_price(iata_code)
    set_lowest_price(row, list(min_price.keys())[0])
    set_lowest_price_date(row, list(min_price.values())[0])
    stops = set_stops(row, get_stops())
    row += 1
for row in compare_prices():
    msg = (f'Alert! INR {row["lowestprice"]} to fly from {SOURCE_IATA} to {row["iatacode"]}, with {stops} stopsm on '
           f'{row["date"]} until {END_DATE}')
    sms(msg)
    whatsapp(msg)

user_data = fill_form()
set_user_data(user_data)
emails = get_user_data()
for email in emails:
    mail(msg, email)

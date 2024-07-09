import smtplib
import time
from datetime import datetime as dt

import requests

host = 'smtp.gmail.com'
port = 587
from_ = 'anuj.nits2@gmail.com'
to_ = 'anuj.nits@gmail.com'
password = 'wzgpcyhchhcdoret'
subject = 'Subject:Look Up'
body = 'ISS is above you in the sky'
msg = f'{subject}\n\n{body}'

my_lat = 51.507351
my_long = -0.127758


def is_iss_overhead():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()
    iss_lat = float(data['iss_position']['latitude'])
    iss_long = float(data['iss_position']['longitude'])
    return abs(iss_lat - my_lat) <= 5 and abs(iss_long - my_long) <= 5


def is_night():
    parameters = {
        'lat': my_lat,
        'lng': my_long,
        'formatted': 0,
    }
    response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    hour_now = dt.now().hour
    return hour_now >= sunset or hour_now <= sunrise


def send_mail():
    if is_iss_overhead() and is_night():
        with smtplib.SMTP(host, port) as conn:
            conn.starttls()
            conn.login(user=from_, password=password)
            conn.sendmail(from_addr=from_, to_addrs=to_, msg=msg)


while True:
    time.sleep(60)
    send_mail()

import random
import smtplib
from datetime import datetime as dt

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

from_ = 'anuj.nits2@gmail.com'
to_ = 'anuj.nits@gmail.com'
pass_ = 'wzgpcyhchhcdoret'
host = 'smtp.gmail.com'
port = 587
message = 'Subject:Quote of the day\n\n'


def get_quote():
    with open('quotes.txt') as f:
        quotes = f.readlines()
        formatted_data = [x.strip('\n') for x in quotes]
        return random.choice(formatted_data)


def get_day():
    return days[dt.now().weekday() - 1]


def send_mail():
    with smtplib.SMTP(host, port) as conn:
        conn.starttls()
        conn.login(from_, pass_)
        conn.sendmail(from_addr=from_, to_addrs=to_, msg=message + get_quote())


send_mail()

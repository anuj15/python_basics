import random
import smtplib
from datetime import datetime as dt

import pandas

host = 'smtp.gmail.com'
port = 587
from_email = 'anuj.nits2@gmail.com'
to_email = 'anuj.nits@gmail.com'
password = 'wzgpcyhchhcdoret'
subject = 'Subject:Hello'
body = 'This is the body of my email'

data = pandas.read_csv('birthdays.csv').to_dict(orient='records')
current_month = dt.now().month
current_date = dt.now().day
birthday_person = ''
for row in data:
    if current_date == row['day'] and current_month == row['month']:
        birthday_person = row['name']
if len(birthday_person) > 0:
    letter_number = random.randint(1, 3)
    with open(f'letter_templates/letter_{letter_number}.txt') as f:
        letter_data = f.readlines()
        letter_data = ''.join(letter_data).replace('[NAME]', birthday_person)
        with smtplib.SMTP(host, port) as connection:
            connection.starttls()
            connection.login(user=from_email, password=password)
            connection.sendmail(from_addr=from_email, to_addrs=to_email, msg=f'Subject:Happy Birthday\n\n{letter_data}')

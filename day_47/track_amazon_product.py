import smtplib

import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0',
    'Accept-Language': 'en-US,en;q=0.9',
}
host = 'smtp.gmail.com'
port = 587
user = 'anuj.nits2@gmail.com'
from_ = 'anuj.nits2@gmail.com'
to_ = 'anuj.nits@gmail.com'
password = 'wzgpcyhchhcdoret'


def get_soup():
    response = requests.get(url=url, headers=headers).content
    soup = BeautifulSoup(response, 'lxml')
    return soup


def get_price(soup):
    return float(soup.find(name='span', class_='aok-offscreen').text.strip().split('$')[1])


def get_product_title(soup):
    return soup.find(name='span', id='productTitle').text.strip()


def send_mail(msg):
    with smtplib.SMTP(host=host, port=port) as conn:
        conn.starttls()
        conn.login(user=user, password=password)
        conn.sendmail(from_addr=from_, to_addrs=to_, msg=msg)


my_price = 100
soup_ = get_soup()
current_price = get_price(soup_)
product_title = get_product_title(soup_)
msg_ = f'subject: Low Price Alert\n\nGet {product_title} at ${current_price}\n{url}'.encode('utf-8')

if current_price <= my_price:
    send_mail(msg_)

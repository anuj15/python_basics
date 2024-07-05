import smtplib

from twilio.rest import Client

TWILIO_SID = 'AC223ecbcc3ac60900229dd2c0628095f6'
TWILIO_AUTH_TOKEN = '958f5c4471ecc9f9362f097358336765'
TWILIO_PHONE_NO = '+19542105492'
TWILIO_WHATSAPP_NO = 'whatsapp:+14155238886'
MY_PHONE_NO = '+916351838207'
MY_WHATSAPP_NO = 'whatsapp:+916351838207'
SERVER = 'smtp.gmail.com'
PORT = 587
FROM_ = 'anuj.nits2@gmail.com'
PWD = 'wzgpcyhchhcdoret'
SUBJECT = 'LOW FARE ALERT!\n\n'


def sms(msg):
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
        from_=TWILIO_PHONE_NO,
        body=msg,
        to=MY_PHONE_NO
    )


def whatsapp(msg):
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
        from_=TWILIO_WHATSAPP_NO,
        body=msg,
        to=MY_WHATSAPP_NO
    )


def mail(msg, to_):
    with smtplib.SMTP(SERVER, PORT) as conn:
        conn.starttls()
        conn.login(FROM_, PWD)
        conn.sendmail(FROM_, to_, f'{SUBJECT}{msg}')

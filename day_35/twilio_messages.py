from twilio.rest import Client

TWILIO_SID = 'AC223ecbcc3ac60900229dd2c0628095f6'
TWILIO_AUTH_TOKEN = '1bee20975ad1c6327b680c76bb7d4b43'
TWILIO_PHONE_NO = '+19542105492'
TWILIO_WHATSAPP_NO = 'whatsapp:+14155238886'
MY_PHONE_NO = '+916351838207'
MY_WHATSAPP_NO = 'whatsapp:+916351838207'


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

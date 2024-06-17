import smtplib

server = 'smtp.gmail.com'
from_email = 'anuj.nits2@gmail.com'
to_email = 'anuj.nits@gmail.com'
password = 'wzgpcyhchhcdoret'
subject = 'Subject:Hello'
body = 'This is the body of my email'

with smtplib.SMTP(server, port=587) as connection:
    connection.starttls()
    connection.login(user=from_email, password=password)
    connection.sendmail(from_addr=from_email, to_addrs=to_email, msg=f'{subject}\n\n{body}')

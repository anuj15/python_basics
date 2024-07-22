import smtplib

import requests
from flask import Flask, render_template, request

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index1.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html")
    else:
        msg = (f'Subject: New Message\n\nName: {request.form["name"]}\nEmail: {request.form["email"]}\nPhone: '
               f'{request.form["phone"]}\nMessage:{request.form["message"]}')
        send_mail(msg)
        return render_template("contact.html", msg='Successfully sent message')


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


def send_mail(msg):
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as conn:
        conn.starttls()
        conn.login(user='anuj.nits2@gmail.com', password='wzgpcyhchhcdoret')
        conn.sendmail(from_addr='anuj.nits2@gmail.com', to_addrs='anuj.nits@gmail.com', msg=msg)


if __name__ == "__main__":
    app.run(debug=True, port=5001)

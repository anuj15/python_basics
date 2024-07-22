from datetime import datetime as dt
import requests
from flask import Flask, render_template

app = Flask(__name__)
all_posts = requests.get('https://api.npoint.io/674f5423f73deab1e9a7').json()
today = dt.now().strftime('%Y-%m-%d')


@app.route('/')
def home():
    return render_template('index1.html', posts=all_posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:num>')
def post(num):
    return render_template('post.html', num=num - 1, posts=all_posts, author='Anuj Gupta', date=today)


if __name__ == '__main__':
    app.run(debug=True)

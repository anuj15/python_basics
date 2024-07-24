import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/blogs')
def blogs():
    all_posts = requests.get('https://api.npoint.io/a206fc26efb5d2dda1fe').json()
    return render_template('blogs.html', blogs=all_posts)


@app.route('/blog/<int:num>')
def specific_blog(num):
    all_posts = requests.get('https://api.npoint.io/a206fc26efb5d2dda1fe').json()
    return render_template('blog.html', blogs=all_posts, num=num)


if __name__ == '__main__':
    app.run(debug=True, port=8080)

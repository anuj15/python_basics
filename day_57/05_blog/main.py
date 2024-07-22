import requests
from flask import Flask, render_template

app = Flask(__name__)
blogs = requests.get('https://api.npoint.io/c790b4d5cab58020d391', verify=False).json()


@app.route('/')
def home():
    return render_template("index.html", blogs=blogs)


@app.route('/post/<int:num>')
def post(num):
    return render_template('post.html', num=num, blogs=blogs)


if __name__ == "__main__":
    app.run(debug=True, port=8080)

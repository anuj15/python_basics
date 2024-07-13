from datetime import datetime as dt

import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    current_year = dt.now().year
    return render_template('index.html', year=current_year)


@app.route('/guess/<name>')
def guess_data(name):
    age = requests.get(f'https://api.agify.io?name={name}').json()['age']
    gender = requests.get(f'https://api.genderize.io?name={name}').json()['gender']
    return render_template('guess.html', name=name.title(), age=age, gender=gender)


if __name__ == '__main__':
    app.run(debug=True)

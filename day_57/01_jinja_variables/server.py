import random
from datetime import datetime as dt
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = dt.now().year
    return render_template('index1.html', num=random_number, year=current_year)


if __name__ == '__main__':
    app.run(debug=True)

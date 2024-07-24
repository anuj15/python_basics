from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Home'


@app.route('/username/1/<name>')
def greetings_1(name):
    return f'1. Hello {name}!'


@app.route('/username/2/<path:name>')
def greetings_2(name):
    return f'2. Hello there {name}!'


@app.route('/username/3/<name>/2A')
def greetings_3(name):
    return f'3. Hello there {name}!'


@app.route('/username/4/<path:name>/<int:number>')
def greetings_4(name, number):
    return f'4. Hello there {name}, you are {number} year(s) old!'


if __name__ == '__main__':
    app.run(debug=True, port=8080)

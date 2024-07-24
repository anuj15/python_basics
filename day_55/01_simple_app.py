from flask import Flask

app = Flask(__name__)


@app.route('/')
def say_home():
    return 'Home'


@app.route('/<name>')
def greetings(name):
    return f'Hello there {name + str(12)}'


if __name__ == '__main__':
    app.run(debug=True, port=8080)

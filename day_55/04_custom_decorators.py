from flask import Flask

app = Flask(__name__)


def make_bold(func):
    def wrapper_func():
        return f'<b>{func()}</b>'

    return wrapper_func


def make_emphasized(func):
    def wrapper_func():
        return f'<em>{func()}</em>'

    return wrapper_func


def make_underlined(func):
    def wrapper_func():
        return f'<u>{func()}</u>'

    return wrapper_func


@app.route('/')
@make_bold
@make_emphasized
@make_underlined
def bye():
    return 'Bye!'


if __name__ == '__main__':
    app.run(debug=True)

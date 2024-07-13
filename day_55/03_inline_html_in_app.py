from flask import Flask

app = Flask(__name__)


@app.route('/')
def one():
    return 'home'


@app.route('/1')
def two():
    return ('<h1 style="text-align:center">Hello World</h1>'
            '<p>This is a paragraph</p>'
            '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExb3Jmb3lvZDVraTRlb3ZzcG9yd2ptNGZnazF1eTM4M3JoYXdhOHg'
            'yaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o72FgntqDRk1eAkr6/giphy.gif" width=500, height=300, alt="cute'
            ' girl">'
            )


@app.route('/bye')
def bye():
    return '<b>Bye</b>'


if __name__ == '__main__':
    app.run(debug=True)

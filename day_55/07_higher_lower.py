import random

from flask import Flask

app = Flask(__name__)
computer = random.randint(0, 9)


@app.route('/')
def home():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=200, height=200>')


@app.route('/<int:num>')
def guess(num):
    if num == computer:
        return ('<h1 style="color:green">You got it</h1>'
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=200, height=200>')
    elif num < computer:
        return ('<h1 style="color:red">Too Low, Try Again!</h1>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=200, height=200>')
    else:
        return ('<h1 style="color:blue">Too High, Try Again!</h1>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=200, height=200>')


if __name__ == '__main__':
    app.run(debug=True)

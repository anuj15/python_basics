from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

from wtf_forms import MyForm

app = Flask(__name__)
app.secret_key = "some secret string"
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = MyForm()
    if form.email.data == '1@1.1' and form.password.data == '12345678':
        return render_template('success.html')
    if form.validate_on_submit():
        return render_template('denied.html')
    else:
        return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=8080)

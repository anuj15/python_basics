from flask import Flask, render_template

from wtf_forms import MyForm

app = Flask(__name__)
app.secret_key = 'a random string'


@app.route("/")
def home():
    return render_template('index1.html')


@app.route("/login", methods=['POST', 'GET'])
def login():
    login_form = MyForm()
    login_form.validate_on_submit()
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

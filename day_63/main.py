from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column
from wtforms import StringField, FloatField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
Bootstrap5(app)
db = SQLAlchemy()
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


with app.app_context():
    db.create_all()


class MyForm(FlaskForm):
    title = StringField(label='Book Name', validators=[DataRequired()])
    author = StringField(label='Book Author', validators=[DataRequired()])
    rating = FloatField(label='Rating', validators=[DataRequired()])
    submit = SubmitField(label='Ok')


class EditForm(FlaskForm):
    new_rating = TextAreaField(label='New Rating', validators=[DataRequired()], description='Enter new rating')
    submit = SubmitField(label='Change Rating')


@app.route('/')
def home():
    books = db.session.execute(db.select(Book)).scalars().all()
    return render_template('index.html', data=books)


@app.route("/add", methods=['POST', 'GET'])
def add():
    form = MyForm()
    if form.validate_on_submit():
        book = Book(title=form.title.data, author=form.author.data, rating=form.rating.data)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)


@app.route("/edit/<int:book_id>", methods=['POST', 'GET'])
def edit(book_id):
    book_to_update = db.get_or_404(Book, book_id)
    form = EditForm()
    if form.validate_on_submit():
        book_to_update.rating = form.new_rating.data
        db.session.commit()
        return redirect(url_for('home'))
    books = db.session.execute(db.select(Book)).scalars()
    return render_template('edit.html', data=books, book_id=book_id, form=form)


@app.route('/delete')
def delete():
    book_id = request.args.get('book_id')
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True, port=8080)

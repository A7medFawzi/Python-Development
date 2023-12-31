from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120),unique=False, nullable=False)
    author = db.Column(db.String(120),unique=False, nullable=False)
    rating = db.Column(db.Float,unique=False)

    def __repr__(self):
        return f'<Book{self.title}>'


db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(Book).all()

    return render_template("index.html", books=all_books)


@app.route("/edit", methods=["POST", "GET"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        book_to_update = Book.query.get(book_id)
        book_to_update.rating= request.form["ratting"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    return render_template("ratting.html", book=book_selected)

@app.route("/delete")
def delete():
    book_id = request.args.get('id')

    # DELETE A RECORD BY ID
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        book_name = request.form['name']
        book_author = request.form['author']
        ratting = request.form['ratting']
        new_book = Book(title=book_name, author=book_author, rating=ratting)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

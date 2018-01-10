from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from flask_pymongo import PyMongo

app = FlaskAPI(__name__)

app.config['MONGO_DBNAME'] = 'reed_book_server'
mongo = PyMongo(app)


@app.route("/<book_name>")
def book_indices(book_name):
    pass


@app.route("/book/", methods=['POST', 'GET'])
def book_chapter():
    book = mongo.db.books.find_one_or_404({'book_name': str(request.data.get('book_name', ''))})
    return book['book_sites']['chapters'][int(request.data.get('chapter_index', 0))]


if __name__ == "__main__":
    app.run(debug=True)

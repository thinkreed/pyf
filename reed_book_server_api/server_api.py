from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)


@app.route("/<book_name>")
def book_indices(book_name):
    pass


@app.route("/<book_name>/<int:index>")
def book_chapter(book_name, index):
    pass


if __name__ == "__main__":
    app.run(debug=True)

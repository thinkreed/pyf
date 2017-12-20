from pymongo import MongoClient


class BookSaver:
    def __init__(self):
        mongo_client = MongoClient('localhost', 27017)
        self.books = mongo_client.book_db

    def insert_chapter(self, book_name, chapter):
        book_chapter = {
            'book_name': book_name,
            'chapter_title': chapter['chapter_title'],
            'index': chapter['index'],
            'url': chapter['url']
        }
        self.books[book_name].insert_one(book_chapter)

    def get_chapter_by_index(self, index, book_name):
        return self.books[book_name].find_one({'index': index})

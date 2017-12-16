from pymongo import MongoClient


class BookSaver:
    def __init__(self):
        mongo_client = MongoClient('mongodb://book.server:27017')
        self.book_db = mongo_client.book_db

    def insert_chapter(self, book_name, chapter):
        pass
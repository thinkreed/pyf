import json

from bserver.book_fetcher import BookFetcher
from bserver.workers import Workers


def load_from_json_file(path):
    with open(path, 'r') as rf:
        return json.load(rf)


def dump_to_json_file(path, json_object):
    with open(path, 'w') as wf:
        json.dump(json_object, wf)


if __name__ == '__main__':
    workers = Workers()
    book_fetcher = BookFetcher('https://www.qu.la')
    workers.get_worker().submit(book_fetcher.start)

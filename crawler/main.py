import requests
from bs4 import BeautifulSoup
import json
import os
from workers import Workers


def get_all_books(response):
    soup = BeautifulSoup(response.text, 'html5lib')
    books = {}
    for a_tag in soup.find_all('a'):
        if is_book_path(a_tag['href']) and a_tag.text.strip():
            books[a_tag.text.strip()] = url_base + a_tag['href']
    return books


def temp():
    if not os.path.exists('../output/'):
        os.makedirs('../output/')


def load_from_json_file(path):
    with open(path, 'r') as rf:
        return json.load(rf)


def dump_to_json_file(path, json_object):
    with open(path, 'w') as wf:
        json.dump(json_object, wf)


def is_book_path(path):
    return '/book/' in path and '.html' not in path


def start():
    destination_url = 'https://www.qu.la'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
    }
    response = requests.get(destination_url, headers=headers)
    books = get_all_books(response)
    parse_books(books)


def parse_books(books):
    for book_name, book_url in books.items():
        workers.get_worker().submit(parse_book, book_name, book_url)


def parse_book(book_name, book_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
    }
    response = requests.get(book_url, headers=headers)
    chapters = get_all_chapters(response)
    print(chapters)


def get_all_chapters(response):
    soup = BeautifulSoup(response.text, 'html5lib')
    chapters = {}
    for dd_tag in soup.find_all('dd'):
        if not dd_tag.a:
            continue
        a_tag = dd_tag.a
        if is_chapter_url(a_tag['href']):
            chapters[a_tag.text.strip()] = url_base + a_tag['href'].strip()
    return chapters


def is_chapter_url(chapter_path):
    return '.html' in chapter_path and '/book/' in chapter_path


workers = Workers()
url_base = 'https://www.qu.la'


def main():
    workers.get_worker().submit(start)


main()

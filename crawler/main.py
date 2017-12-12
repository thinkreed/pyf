import requests
from bs4 import BeautifulSoup
from threading import Thread
import json
import os


def get_all_a_tag(response):
    soup = BeautifulSoup(response.text, 'html5lib')
    books = {}
    url_base = 'https://www.qu.la'
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


def main():
    destination_url = 'https://www.qu.la'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
    }
    response = requests.get(destination_url, headers=headers)
    parse_thread = Thread(target=get_all_a_tag, args=(response,))
    parse_thread.start()
    parse_thread.join()


main()

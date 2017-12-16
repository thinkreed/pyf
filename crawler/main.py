import requests
from bs4 import BeautifulSoup
import json
import os
from workers import Workers
import re
from pymongo import MongoClient




def get_all_books(response):
    soup = BeautifulSoup(response.text, 'html5lib')
    books = {}
    for a_tag in soup.find_all('a'):
        if is_book_path(a_tag['href']) and a_tag.text.strip():
            books[a_tag.text.strip()] = url_base + a_tag['href']
    return books


def check_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


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
        parse_book(book_name, book_url)


def parse_book(book_name, book_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
    }
    response = requests.get(book_url, headers=headers)
    chapters = get_all_chapters(response)
    dump_to_json_file(output_directory + '/' + book_name + '.json', chapters)


def parse_chapter(chapters, book_name):
    book_directory = output_directory + '/' + book_name
    check_directory(book_directory)
    for chapter_name, chapter_url in chapters.items():
        get_chapter_content(chapter_name, chapter_url, book_directory)


def get_chapter_content(chapter_name, chapter_url, book_directory):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    }
    response = requests.get(chapter_url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    div_content = soup.find('div', id="content")
    pattern = r'<div id="content">(.*?)</div>'
    try:
        content = re.findall(pattern, str(div_content), re.S)[0]
        content = content.replace('<br/>　　<br/>', '\n')
        content = content.replace('<script>chaptererror();</script>', '')
        content.strip()
        file_path = book_directory + '/' + chapter_name + '.txt'
        with open(file_path, 'w', encoding='utf-8', errors='ignore') as f:
            f.write(content)
    except:
        print('re fail in %s' % chapter_name)


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

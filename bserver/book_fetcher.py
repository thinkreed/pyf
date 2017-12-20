import re

import requests
from bs4 import BeautifulSoup

from bserver.book_saver import BookSaver


class BookFetcher:
    def __init__(self, url_base):
        self.url_base = url_base
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        }
        self.book_saver = BookSaver()

    def get_all_books(self, response):
        soup = BeautifulSoup(response.text, 'html5lib')
        books = {}
        for a_tag in soup.find_all('a'):
            if self.is_book_path(a_tag['href']) and a_tag.text.strip():
                books[a_tag.text.strip()] = self.url_base + a_tag['href']
        return books

    def is_book_path(self, path):
        return '/book/' in path and '.html' not in path

    def start(self):
        response = requests.get(self.url_base, headers=self.headers)
        books = self.get_all_books(response)
        self.parse_books(books)

    def parse_books(self, books):
        for book_name, book_url in books.items():
            self.parse_book(book_name, book_url)

    def parse_book(self, book_name, book_url):
        response = requests.get(book_url, headers=self.headers)
        self.get_all_chapters(response, book_name)

    def get_chapter_content(self, chapter_name, chapter_url):
        response = requests.get(chapter_url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'lxml')
        div_content = soup.find('div', id="content")
        pattern = r'<div id="content">(.*?)</div>'
        try:
            content = re.findall(pattern, str(div_content), re.S)[0]
            content = content.replace('<br/>　　<br/>', '\n')
            content = content.replace('<script>chaptererror();</script>', '')
            content.strip()
            return content
        except:
            print('re fail in %s' % chapter_name)

    def get_all_chapters(self, response, book_name):
        soup = BeautifulSoup(response.text, 'html5lib')
        index = 1
        for dd_tag in soup.find_all('dd'):
            if not dd_tag.a:
                continue
            a_tag = dd_tag.a
            if self.is_chapter_url(a_tag['href']):
                self.book_saver.insert_chapter(book_name, {
                    'chapter_title': a_tag.text.strip(),
                    'index': index,
                    'url': self.url_base + a_tag['href'].strip()
                })
                index += 1

    def fetch_chapter_content_by_index(self, index, book_name):
        chapter = self.book_saver.get_chapter_by_index(index, book_name)
        return self.get_chapter_content(chapter['chapter_title'], chapter['url'])

    def is_chapter_url(self, chapter_path):
        return '.html' in chapter_path and '/book/' in chapter_path

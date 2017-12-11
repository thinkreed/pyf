import requests
from bs4 import BeautifulSoup
from threading import Thread


def get_all_a_tag(response):
    soup = BeautifulSoup(response.text)
    for a_tag in soup.find_all('a'):
        print(a_tag['href'])


def main():
    destination_url = 'https://www.qu.la'
    response = requests.get(destination_url)
    parse_thread = Thread(target=get_all_a_tag, args=(response,))
    parse_thread.start()
    parse_thread.join()


main()

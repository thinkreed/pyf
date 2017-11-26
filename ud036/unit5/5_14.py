import requests


def read_text_from_file(path):
    with open(path, 'r') as quotes:
        return quotes.read()


def check_profanity(text):
    response = requests.get('http://www.wdyl.com/profanity?q=' + text)
    print(response)
    if 'True' in response.text:
        return False

    if 'False' in response.text:
        return True

    print('the response is not correct')


def test():
    text = read_text_from_file(r'/Users/thinkreed/Downloads/movie_quotes.txt')
    has_profanity = check_profanity(text)
    if has_profanity:
        print('alert profanity')
    else:
        print('it is ok')


test()

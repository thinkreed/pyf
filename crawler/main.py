import requests


def main():
    content = requests.get('https://www.baidu.com')
    print(content.content)


main()
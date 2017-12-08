import requests


def main():
    content = requests.get('https://www.baidu.com')
    index = content.content.find('<h2')
    print(index)


main()

import requests
import os

payload = {'book_name': '一念永恒', 'index': 1}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
response = requests.get('http://localhost:8168', headers=headers, params=payload)
print(response.url)

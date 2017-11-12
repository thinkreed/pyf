index = []


def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword, [url]])


def add_page_to_index(index, url, content):
    for keyword in content.split():
        add_to_index(index, keyword, url)


add_page_to_index(index, 'fake.text', "This is a test")
print(index)

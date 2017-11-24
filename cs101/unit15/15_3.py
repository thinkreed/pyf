index = [['udacity', ['http://udacity.com', 'http://npr.org']],
         ['computing', ['http://acm.org']]]


def lookup(index,keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]

    return []


print(lookup(index, 'udacity'))
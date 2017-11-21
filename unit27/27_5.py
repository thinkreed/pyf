def make_converter(match, replacement):
    return {match: replacement}


def apply_converter(converter, string):
    match, replacement = converter.popitem()
    start = string.find(match)
    while start != -1:
        string = string[:start] + replacement + string[start + len(match):]
        start = string.find(match)

    return string


c1 = make_converter('aa', 'a')
print(apply_converter(c1, 'aaaa'))

c = make_converter('aba', 'b')
print(apply_converter(c, 'aaaaaabaaaaa'))

def remove_html_tags(s):
    is_in_tag_mode = False
    output = ''

    for c in s:
        if c == '<':
            is_in_tag_mode = True
            continue

        if c == '>':
            is_in_tag_mode = False
            continue

        if not is_in_tag_mode:
            output += c

    return output


def test():
    print(remove_html_tags('<b>foo</b>'))


test()
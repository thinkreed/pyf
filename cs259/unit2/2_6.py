def remove_html_tags(s):
    is_in_tag_mode = False
    quote = False
    output = ''

    for c in s:
        if c == '<' and not quote:
            is_in_tag_mode = True
            continue

        if c == '>' and not quote:
            is_in_tag_mode = False
            continue

        if c == '"' or c == "." and is_in_tag_mode:
            quote = not quote
            continue

        if not is_in_tag_mode:
            output += c

    return output


def test():
    print(remove_html_tags('<a href=">">foo</a>'))


test()
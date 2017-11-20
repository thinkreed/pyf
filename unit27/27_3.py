def remove_tags(content):
    result = []
    current_word = ''
    for char in content:
        if char == ' ':
            if len(current_word) > 0 and current_word[0] != '<':
                result.append(current_word)
                current_word = ''
            continue

        if char == '<':
            if len(current_word) and current_word[0] != '<':
                result.append(current_word)
                current_word = ''
            current_word += '<'
            continue

        if char == '>':
            current_word = ''
            continue

        if len(current_word) > 0 and current_word[0] == '<':
            continue

        current_word += char
    if len(current_word) > 0:
        result.append(current_word)
    return result


print(remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>'''))
print(remove_tags('''<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>'''))
print(remove_tags("<hello><goodbye>"))
print(remove_tags("This is plain text."))

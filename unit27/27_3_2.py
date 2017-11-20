def remove_tags(content):
    start = content.find('<')
    while start != -1:
        end = content.find('>', start)
        content = content[:start] + " " + content[end + 1:]
        start = content.find('<')
    return content.split()


print(remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>'''))
print(remove_tags('''<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>'''))
print(remove_tags("<hello><goodbye>"))
print(remove_tags("This is plain text."))
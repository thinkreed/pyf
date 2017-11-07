page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')

start_link = page.find('<a href=')

left_quote = page.find('"', start_link)
right_quote = page.find('"', left_quote + 1)

url = page[left_quote + 1:right_quote]

print(url)
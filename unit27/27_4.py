english = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May",
           6: "June", 7: "July", 8: "August", 9: "September", 10: "October",
           11: "November", 12: "December"}

swedish = {1: "januari", 2: "februari", 3: "mars", 4: "april", 5: "maj",
           6: "juni", 7: "juli", 8: "augusti", 9: "september", 10: "oktober",
           11: "november", 12: "december"}


def date_converter(month_dictionary, date):
    start = date.find('/')
    month = month_dictionary[int(date[:start])]
    end = date.find('/', start + 1)
    day = date[start + 1:end]
    year = date[end + 1:]
    return day + ' ' + month + ' ' + year


def date_converter2(month_dictionary, date):
    month, day, year = date.split('/')
    return day + ' ' + month_dictionary[int(month)] + ' ' + year


print(date_converter(english, '5/11/2012'))
print(date_converter(english, '5/11/12'))
print(date_converter(swedish, '5/11/2012'))
print(date_converter2(swedish, '12/5/1791'))

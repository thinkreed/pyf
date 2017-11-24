def numbers_in_lists(string):
    result = []

    preceding = int(string[0]) - 1
    sublist = []
    for char in string:
        number = int(char)
        if number > preceding:
            if sublist:
                result.append(sublist)
                sublist = []
            result.append(number)
            preceding = number
        else:
            sublist.append(number)
    if sublist:
        result.append(sublist)

    return result


string = '543987'
result = [5,[4,3],9,[8,7]]
print(numbers_in_lists(string))
string= '987654321'
result = [9,[8,7,6,5,4,3,2,1]]
assert repr(string), numbers_in_lists(string) == result
string = '455532123266'
result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
assert repr(string), numbers_in_lists(string) == result
string = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert repr(string), numbers_in_lists(string) == result
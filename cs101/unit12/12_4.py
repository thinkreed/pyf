def greatest(list_of_numbers):
    result = 0
    for number in list_of_numbers:
        if number > result:
            result = number

    return result


print(greatest([4, 23, 1]))
print(greatest([]))

def product_list(list_of_numbers):
    result = 1
    for number in list_of_numbers:
        result = result * number

    return result


print(product_list([1, 2, 3, 4]))

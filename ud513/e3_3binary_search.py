def binary_search(input_array, value):
    """Your code goes here."""
    i, j = 0, len(input_array) - 1
    while i <= j:
        half = (i + j) // 2
        if value < input_array[half]:
            j = half - 1
        elif value > input_array[half]:
            i = half + 1
        else:
            return half
    return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))

print(binary_search(test_list, test_val2))


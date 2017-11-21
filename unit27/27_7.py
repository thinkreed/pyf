def is_list(p):
    return isinstance(p, list)

def deep_reverse(input_list):
    result_list = []

    i = len(input_list) - 1
    while i >= 0:
        if is_list(input_list[i]):
            result_list.append(deep_reverse(input_list[i]))
        else:
            result_list.append(input_list[i])
        i -= 1
    return result_list



p = [1, [2, 3, [4, [5, 6]]]]
print(deep_reverse(p))

print(p)

q =  [1, [2,3], 4, [5,6]]
print(deep_reverse(q))
print(q)

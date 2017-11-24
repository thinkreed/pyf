def is_list(p):
    return isinstance(p, list)


def deep_count(p):
    sum = 0
    for e in p:
        sum += 1
        if is_list(e):
            sum += deep_count(e)
    return sum



print(deep_count([1, 2, 3]))
print(deep_count([1, [], 3]))
print(deep_count([1, [1, 2, [3, 4]]]))
print(deep_count([[[[[[[[1, 2, 3]]]]]]]]))

def longest_repetition(p):
    best = None
    lenth = 0
    current = None
    current_lenth = 0
    for e in p:
        if current == e:
            current_lenth += 1
        else:
            current_lenth = 1
            current = e

        if current_lenth > lenth:
            best = current
            lenth = current_lenth

    return best


print(longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1]))
print(longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd']))
print(longest_repetition([1,2,3,4,5]))
print(longest_repetition([]))

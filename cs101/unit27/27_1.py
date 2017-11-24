def pick_one(first_or_second, first, second):
    if first_or_second:
        return first
    else:
        return second


print(pick_one(True, 37, 'hello'))
# >>> 37

print(pick_one(False, 37, 'hello'))
# >>> hello

print(pick_one(True, 'red pill', 'blue pill'))
# >>> red pill

print(pick_one(False, 'sunny', 'rainy'))
# >>> rainy

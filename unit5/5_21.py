def biggest(a, b, c):
    result = a

    if b > result:
        result = b

    if c > result:
        result = c

    return result

print(biggest(3, 2, 8))
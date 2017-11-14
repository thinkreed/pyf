def hash_string(keyword, buckets):
    ord_sum = 0
    for char in keyword:
        ord_sum = (ord_sum + ord(char)) % buckets
    return ord_sum


print(hash_string('a', 12))
print(hash_string('b', 12))
print(hash_string('a', 13))
print(hash_string('au', 12))
print(hash_string('udacity', 12))

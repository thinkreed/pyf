def make_hashtable(nbuckets):
    empty_hash_table = []
    i = 0
    while i < nbuckets:
        empty_hash_table.append([])
        i += 1
    return empty_hash_table


print(make_hashtable(5))
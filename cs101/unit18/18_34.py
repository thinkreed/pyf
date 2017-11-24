def lookup(index, keyword):
    if keyword not in index:
        return None

    return index[keyword]
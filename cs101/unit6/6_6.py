def find_last(search_string, target_string):
    last_index = search_string.find(target_string)

    if last_index == -1:
        return -1

    while True:
        current_index = search_string.find(target_string, last_index + 1)
        if current_index == -1:
            break
        last_index = current_index

    return last_index

print(find_last("222222222", ""))
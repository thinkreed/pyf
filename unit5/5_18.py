def is_friend(name):
    if name[0] == 'D':
        return True

    if name[0] == 'N':
        return True

    return False

print(is_friend('Nani'))
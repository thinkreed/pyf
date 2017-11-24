def shift(letter):
    shift_value = (ord(letter) - ord('a') + 1) % 26
    return chr(ord('a') + shift_value)


print(shift('a'))
print(shift('n'))
print(shift('z'))

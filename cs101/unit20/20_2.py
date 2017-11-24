def shift_n_letters(letter, n):
    shift_value = (ord(letter) - ord('a') + (n % 26)) % 26
    return chr(ord('a') + shift_value)


print(shift_n_letters('s', 1))
print(shift_n_letters('s', 2))
print(shift_n_letters('s', 10))
print(shift_n_letters('s', -10))
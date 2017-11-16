def shift_n_letters(letter, n):
    shift_value = (ord(letter) - ord('a') + (n % 26)) % 26
    return chr(ord('a') + shift_value)


def rotate(letters, n):
    result = ''
    for letter in letters:
        if letter == ' ':
            result += letter
        else:
            result += shift_n_letters(letter, n)
    return result


print(rotate('sarah', 13))
print(rotate('fnenu', 13))
print(rotate('dave', 5))
print(rotate('ifaj', -5))
print(rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
              "sv rscv kf ivru kyzj"), -17))

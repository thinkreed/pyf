def is_palindrome(s):
    if len(s) == 0:
        return True

    if s[0] != s[-1]:
        return False

    return is_palindrome(s[1:-1])


print(is_palindrome(''))
print(is_palindrome('abab'))
print(is_palindrome('abba'))

def is_palindrome(num):
    tmp = num
    total = 0

    while tmp > 0:
        total = total * 10 + tmp % 10
        tmp //= 10

    return total == num


if __name__ == '__main__':
    print is_palindrome(121)
else:
    print 'not main'
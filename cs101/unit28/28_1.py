#  S(n, k) = k*S(n-1, k) + S(n-1, k-1)
def stirling(n, k):
    if n == 0:
        return 0
    if k == 1:
        return 1
    if n == k:
        return 1
    if n < k:
        return 0

    return k * stirling(n - 1, k) + stirling(n - 1, k - 1)


def bell(n):
    result = 0
    for i in range(1, n + 1):
        result += stirling(n, i)
    return result


print(stirling(1, 1))
print(stirling(2, 1))
print(stirling(2, 2))
print(stirling(2, 3))
print(stirling(3, 1))
print(stirling(3, 2))
print(stirling(3, 3))
print(stirling(4, 1))
print(stirling(4, 2))
print(stirling(4, 3))
print(stirling(4, 4))
print(stirling(20, 15))
print(bell(1))
print(bell(2))
print(bell(5))
print(bell(15))

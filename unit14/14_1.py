def antisymmetric(A):

    if len(A) == 0:
        return True

    if len(A) != len(A[0]):
        return False

    n = len(A)

    i = 0
    while i < n:
        j = 0
        while j < n:
            if A[i][j] != - A[j][i]:
                return False
            j = j + 1
        i = i + 1
    return True


assert antisymmetric([[0, 1, 2],
                     [-1, 0, 3],
                     [-2, -3, 0]])

assert antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])

assert not antisymmetric([[0, 1, 2],
                     [-1, 0, -2],
                     [2, 2,  3]])

assert not antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]])
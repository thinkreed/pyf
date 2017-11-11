def is_identity_matrix(matrix):
    if len(matrix) == 0:
        return True

    if len(matrix) != len(matrix[0]):
        return False

    i = 0
    n = len(matrix)
    while i < n:
        j = 0
        while j < n:
            if i == j:
                if matrix[i][j] != 1:
                    return False
            else:
                if matrix[i][j] != 0:
                    return False
            j = j + 1
        i = i + 1
    return True


matrix1 = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]

assert is_identity_matrix(matrix1)

matrix2 = [[1,0,0],
           [0,1,0],
           [0,0,0]]

assert  not is_identity_matrix(matrix2)

matrix3 = [[2,0,0],
           [0,2,0],
           [0,0,2]]

assert not is_identity_matrix(matrix3)

matrix4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

assert not is_identity_matrix(matrix4)

matrix5 = [[1,0,0,0,0,0,0,0,0]]

assert  not is_identity_matrix(matrix5)

matrix6 = [[1,0,0,0],
           [0,1,0,1],
           [0,0,1,0],
           [0,0,0,1]]

assert  not is_identity_matrix(matrix6)

matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]
assert  not is_identity_matrix(matrix7)
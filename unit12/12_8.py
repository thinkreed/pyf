correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]


def check_sudoku_first(p):
    n = len(p)
    digit = 1

    while digit <= n:
        i = 0
        while i < n:
            row_count = 0
            column_count = 0
            j = 0
            while j < n:
                if p[i][j] == digit:
                    row_count = row_count + 1

                if p[j][i] == digit:
                    column_count = column_count + 1

                j = j + 1
            
            if column_count != 1 or row_count != 1:
                return False

            i = i + 1
        digit = digit + 1

    return True

    return True


print(check_sudoku_first(correct))
print(check_sudoku_first(incorrect))
print(check_sudoku_first(incorrect2))
print(check_sudoku_first(incorrect3))
print(check_sudoku_first(incorrect4))
print(check_sudoku_first(incorrect5))


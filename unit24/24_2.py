def make_next_row(row):
    result = []
    prev = 0
    for e in row:
        result.append(e + prev)
        prev = e
    result.append(prev)
    return result



def triangle(n):
    result = []
    current = [1]
    for i in range(0, n):
        result.append(current)
        current = make_next_row(current)
    return result


print(triangle(0))
print(triangle(1))
print(triangle(2))
print(triangle(3))
print(triangle(6))
def rabbits(n):
    current = 0
    after = 1
    dead = []
    for i in range(0, n):
        if i < 4:
            current, after = after, current + after
        else:
            current, after = after, current + after - dead[i - 4]
        dead.append(current)

    return current


print(rabbits(6))

s = ''
for i in range(1, 12):
    s += str(rabbits(i)) + ' '

print(s)

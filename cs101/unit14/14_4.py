def freq_analysis(message):
    result = []
    i = 0
    while i < 26:
        result.append(0.0)
        i = i + 1
    az_str = 'abcdefghijklmnopqrstuvwxyz'
    if not message:
        return result
    count = 0
    for char in message:
        count = count + 1
        index = az_str.index(char)
        result[index] = result[index] + 1

    i = 0
    while i < 26:
        result[i] = result[i] / count
        i = i + 1

    return result


print(freq_analysis("abcd"))
print(freq_analysis("adca"))
print(freq_analysis('bewarethebunnies'))

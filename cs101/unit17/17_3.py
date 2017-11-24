def convert_seconds(seconds):
    result = ''
    hour = int(seconds / 3600)
    if hour == 1:
        result = result + '1 hour, '
    else:
        result = result + str(hour) + ' hours, '
    minute = int((seconds - hour * 3600) / 60)
    if minute == 1:
        result = result + '1 minute, '
    else:
        result = result + str(minute) + ' minutes, '
    second = seconds - hour * 3600 - minute * 60
    if second == 1:
        result = result + '1 second'
    else:
        result = result + str(second) + ' seconds'

    return result


print(convert_seconds(3661))
print(convert_seconds(7325))
print(convert_seconds(7261.7))

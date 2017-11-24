size_map = {'kb': 2 ** 10, 'kB': 2 ** 10 * 8, 'Mb': 2 ** 20, 'MB': 2 ** 20 * 8, 'Gb': 2 ** 30, 'GB': 2 ** 30 * 8,
            'Tb': 2 ** 40, 'TB': 2 ** 40 * 8}


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


def download_time(file_size, file_unit, bandwidth, bandwidth_unit):
    seconds = file_size * size_map[file_unit] / (bandwidth * size_map[bandwidth_unit])
    return convert_seconds(seconds)


print(download_time(1024, 'kB', 1, 'MB'))
print(download_time(1024, 'kB', 1, 'Mb'))
print(download_time(13, 'GB', 5.6, 'MB'))
print(download_time(13, 'GB', 5.6, 'Mb'))
print(download_time(10, 'MB', 2, 'kB'))
print(download_time(10, 'MB', 2, 'kb'))
print(download_time(11, 'GB', 5, 'MB'))

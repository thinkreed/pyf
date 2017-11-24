def max_number_of_xp_stamp(value_per_stamp, target):
    number_of_stamps = 0
    while True:
        next_num = number_of_stamps + 1
        if next_num * value_per_stamp > target:
            break
        number_of_stamps = next_num

    return number_of_stamps

def stamps(n):
    target = n
    number_of_5p = max_number_of_xp_stamp(5, target)

    target = target - number_of_5p * 5

    number_of_2p = max_number_of_xp_stamp(2, target)

    target = target - number_of_2p * 2

    number_of_1p = max_number_of_xp_stamp(1, target)

    return number_of_5p, number_of_2p, number_of_1p

print(stamps(29))
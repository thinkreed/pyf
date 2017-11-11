def list_mean(numbers):

    if len(numbers) == 0:
        return 0
    numbers_sum = 0.0
    numbers_sum = 0.0 + sum(numbers)

    return numbers_sum / len(numbers)


print(list_mean([1,2,3,4]))
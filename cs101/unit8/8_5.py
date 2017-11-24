def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False


def is_leap_baby(day, month, year):
    # Write your code after this line.
    if not isLeapYear(year):
        return False

    if month != 2:
        return False

    if day == 29:
        return True

    return False

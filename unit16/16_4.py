def split_string(source,splitlist):
    result = []
    at_split = True
    for char in source:
        if char in splitlist:
            at_split = True
        else:
            if at_split:
                result.append(char)
                at_split = False
            else:
                result[-1] = result[-1] + char

    return result


print(split_string("This is a test-of the,string separation-code!"," ,!-"))
print(split_string("After  the flood   ...  all the colors came out.", " ."))
print(split_string("First Name,Last Name,Street Address,City,State,Zip Code",","))

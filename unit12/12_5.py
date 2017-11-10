udacious_univs = [['Udacity',90000,0]]

usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]


def total_enrollment(list_of_universities):
    total_students_enrolled = 0
    total_fees = 0

    for university in list_of_universities:
        total_students_enrolled = total_students_enrolled + university[1]
        total_fees = total_fees + university[1] * university[2]

    return total_students_enrolled, total_fees


print(total_enrollment(usa_univs))

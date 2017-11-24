speed_of_light = 300000. # km per second

def speed_fraction(time, distance):
    return 1000.0 * distance * 2 / time / speed_of_light



print(speed_fraction(50,5000))
print(speed_fraction(50,10000))
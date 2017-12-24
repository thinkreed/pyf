print("""you enter a dark room with two doors.
do you go through door #1 or door #2""")
door = input("> ")

if door == '1':
    print("there is a giant bear here eating a cheese cake")
    print("what do you do")
    print("1. take the cake")
    print("2. scream the bear")

    bear = input("> ")

    if bear == '1':
        print("the bear eats your face off")
    elif bear == '2':
        print("the bear eats your legs off")
    else:
        print(f"well, doing {bear} is probably better")
        print("bear runs away")
elif door == '2':
    print("you stare into endless abyss at Cthulhu's retina")
    print("1. blueberries")
    print("2. yellow jacked clothesspins")
    print("3. understanding revolvers yelling melodies")

    insanity = input("> ")
    if insanity == '1' or insanity == '2':
        print("your body survives powered by a mind of jello")
    else:
        print("the insanity rots your eyes into a pool of muck")
else:
    print("you stumble around and fall on a knife and die")


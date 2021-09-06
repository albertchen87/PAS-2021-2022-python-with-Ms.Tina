print("You enter a dark room with two doors. Do you go through door 1 or door 2?")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake. What do yo do?")
    print("1. take the cake.")
    print("2. Scream at the bear.")
    print("3. Hi")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. good job!")
    elif bear == "2":
        print("The bear eats your legs off. good job!")
    else:
        print("Well, doing %s is probabily better. bear runs away." % bear)

elif door == "2":
    print("You stare inot the endless abyss at Cthulhu's retina.")
    print("!. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello. Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck. Good job!")
    
elif door == "3":
    print("Pamela will hunt you down when you r asleep")

else:
    print("You stuble around and fall on a knife and die. Good job!")
from sys import exit
def gold_room():
    print("This room is full of gold. How much do you take?")

    next = input("> ")
    if int(next) < 50:
        print("Nice, you're not greedy")
        exit(0)
    elif int(next) >= 50:
        dead("You greedy bastard!")
    else:
        dead("Man, learn to type a number.")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        next = input("> ")
        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next =="taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head!")

    next = input("> ")

    if next == "flee":
        start()
    elif next == "head":
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why,"good job!")
    print("Do you want to relife?")
    yes = input("> ")
    if yes == "yes":
        start(0)
    else:
        exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    next = input("> ")

    if next == "left":
        bear_room()
    elif next =="right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()

'''
1. ???
2. yep
3. I understand all
4. Yea
''' 
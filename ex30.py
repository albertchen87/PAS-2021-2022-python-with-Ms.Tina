# define people as 100
people = 100
# define cars as 0
cars = 0
# define buses as 1500
buses = 1500

# print if cars are more than people
if cars > people:
    print("We should take the cars.")
# print if is false and cars < people
elif cars < people:
    print("We should not take the cars.")
# if if and elif aren't ture, print 
else:
    print("We can't decide.")
# print if buses > cars
if buses > cars:
    print("That's too many buses.")
# print if if is false and buses < cars
elif buses < cars:
    print("Maybe we could take the buses.")
# print if and elif is false
else:
    print("We still can't decide.")
# print if people > buses and people < cars
if people > buses and people < cars:
    print("Alright, let's just take the buses.")
# print if if is false
else:
    print("Fine, Let's stay home then.")

# elif is else with a condition, and else is all other condition that are not include in if and elif
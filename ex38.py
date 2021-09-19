ten_things = "Apples Oranges Crows Telephone Lignt Sugar"

print("Wait there's not 10 things in that list, let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    # take one stuff from more stuff and put it into next one
    next_one = more_stuff.pop()
    # print andding next_one
    print("Adding: ", next_one)
    # add next_one into stuff
    stuff.append(next_one)
    # print the length of stuff
    print("There's %d items now." % len(stuff))
# print stuff
print("There we go: ", stuff)
# print Let's do some things with stuff. 
print("Let's do some things with stuff.")
# print the second thing in stuff
print(stuff[1])
# print the last stuff in stuff
print(stuff[-1])
# take the last thing in stuff and print it out
print(stuff.pop())
# print the joined stuff with " " between each stuff 
print(" ".join(stuff))
# join # with 4 and 5 thing in stuff 
print("#".join(stuff[3:5]))
''' 
2. yes
3. no, i learn java
5. dir(something) is function and class is a group of code
'''
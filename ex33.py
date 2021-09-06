numbers = []
def while_loop(i, x, y):
    while i < x:
        print("At the top i is %d" %i)
        numbers.append(i)

        i = i + y
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)

def for_loop(z, x, y):
    for i in range(z, x+1):
        print("At the top i is %d" %i)
        numbers.append(i)
        # for loop will reset i every time so it will only effect the things after it
        i = i+y
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)

print("The numbers: ")

for num in numbers:
    print(num)

for_loop(0, 10, 1)
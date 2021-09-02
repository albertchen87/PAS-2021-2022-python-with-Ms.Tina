rick = "rick is \"tall\" "
dennis = "dogs\\cat\\cow"
steve = """
Steve is old.\n
He can drive a car now\n
But he's still in high school\n\a
"""

print("my friend " + rick)
print("Dennis likes " + dennis + " a lot")
print(steve)

for i in ["/","- ","|","\\","|", "'"]:
    print("%r\r"%i)

print("%s" % "')")

'''
1. ok
2. may need to print " or is faster
4. %r print out the whole thing including the "" but %s only print the thing in it
'''
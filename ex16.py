from sys import argv

script, filename = argv

print("Opening the file...")
target = open(filename)

print(filename)
print(target.read())

print("We're going to erase %r." % filename)
print("If you don't want that, hit CRTL-C (AC).")
print("If you do want that, hit RETURN.")

input("?")

target.close()
target = open(filename, "w")



print("Truncating the file.  Goodbye!")


print("Now I'm going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.\n")

formatter = """{}
{}
{}
"""

target.write(formatter.format(line1,line2,line3))

target.close()
target = open(filename, "r")

print(target.read())

print("and finally, we close it.")
target.close()

# 4. "w" stands wiping the file clear
# 5. No, open with w will erase the whole file

# import argv
from sys import argv
# set up script and input_file
script, input_file = argv
# define print all
def print_all(f):
    # print the f file
    print(f.read())
# define rewind
def rewind(f):
    # back to the start of the file
    f.seek(0)
#define print a line
def print_a_line(line_count, f):
    # print one line in the file
    print(line_count, f.readline())
# assign current_file as the opened file
current_file = open(input_file)
# print "First let's print the whole file:\n"
print("First let's print the whole file:\n")
# call print_all with current_file
print_all(current_file)
# print "Now let's rewind, kind of like a take."
print("Now let's rewind, kind of like a take.")
# call rewind on current_file
rewind(current_file)
# set current_line as 1
current_line = 1
# print the first line
print_a_line(current_line, current_file)
# set the line as 2, 2
current_line += 1
# print the second line
print_a_line(current_line, current_file)
# set teh line as 3, 3
current_line += 1
#print the third lien
print_a_line(current_line, current_file)

# as it pass through to the function, it become the print a line
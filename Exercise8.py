# combine four stuff together with a space in between
formatter = "{} {} {} {}"
# hi
hi = "hi"

# print the four int combined 
print(formatter.format(1, 2, 3, 4))
# print the four string combined 
print(formatter.format("one", "two", "three", "four"))
# print the 4 bools string combied 
print(formatter.format(True, False, False, True))
# print use the formatter as a format and as a string 
print(formatter.format(formatter, formatter, formatter, formatter))
# print four hi
print(formatter.format(hi,hi,hi,hi))
# give the formatter four strings for it to combine
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
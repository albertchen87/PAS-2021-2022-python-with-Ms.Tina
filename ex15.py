# import argv
from sys import argv
# assign script as one in argv
scirpt = argv
# poen the file for what the use inpput
txt = open(input("enter file name "))
# print the filename and the file
print("your file name is", txt.name)
print(txt.read())
# know the next file
print("Open the next file")
fileName2 = input("File name: ")
# open and print the next file
print("Your file name: %r" %(fileName2))
txt2 = open(fileName2)
print(txt2.read())
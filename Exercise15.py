from sys import argv

scirpt = argv

txt = open(input("enter file name "))

print("your file name is", txt.name)
print(txt.read())

print("Open the next file")
fileName2 = input("File name: ")

print("Your file name: %r" %(fileName2))
txt2 = open(fileName2)
print(txt2.read())
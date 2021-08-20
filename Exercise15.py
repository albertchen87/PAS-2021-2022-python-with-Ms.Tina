from sys import argv

scirpt, fileName = argv

txt = open(fileName)

print("your file name is %r" %(fileName))
print(txt.read())

print("Open the next file")
fileName2 = input("File name: ")

print("Your file name: %r" %(fileName2))
txt2 = open(fileName2)
print(txt2.read())
from sys import argv

script, username = argv
prompt = '> '

print("Hi %s, this is %s" % (username, script))
print("How are you %s " % (username))
response = input(prompt)

print("so you are %r" % (response))
print(1<2)

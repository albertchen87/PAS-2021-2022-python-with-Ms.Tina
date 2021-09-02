from sys import argv

script, username, filename = argv
prompt = 'Rick: '

print("Hi %s, this is %s, I see you like %s" % (username, script, filename))
print("How are you %s " % (username))
response = input(prompt)

print("so you are %r" % (response))
print(1<2)

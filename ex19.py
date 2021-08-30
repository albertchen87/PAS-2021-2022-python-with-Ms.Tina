# define the function of cheese_and_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # print how many cheese you have
    print("You have %d cheeses!" % cheese_count)
    # print how many boxes you have
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    # print "man that's enough for a party!"
    print("man that's enough for a party!")
    # print "get a blanket.\n"
    print("get a blanket.\n")

# print "We can just give the function numbers directly:"
print("We can just give the function numbers directly:")
# call cheese_and_crackter with paramiter of 20 and 30
cheese_and_crackers(20, 30)

# prin "OR, we can use variables from our script:"t 
print("OR, we can use variables from our script:")
# define amount_of_cheese as 10
amount_of_cheese = 10
# define amount_of_crackers as 51
amount_of_Crackers =51

# call cheese_and_crackers with amount of cheese and amount of crackers
cheese_and_crackers(amount_of_cheese, amount_of_Crackers)

# print "We can even do matn inside too:"
print("We can even do matn inside too:")
# call cheese and crackers with 10 + 20 and 5 + 6
cheese_and_crackers(10 + 20, 5 + 6)

# print "And we can combine the two, variables and math:"t 
print("And we can combine the two, variables and math:")
# call cheese and crackers with amount of cheese + 100 and amount of crackers + 1000
cheese_and_crackers(amount_of_cheese + 100, amount_of_Crackers + 1000)


def desperate(args):
    print(args)

desperate(1)
desperate(20)
desperate("HI")
desperate("IDK")
desperate("hello")
desperate(3)
desperate(5)
desperate(8)
desperate("I'm dying")
desperate("help me")
desperate("bubbles")

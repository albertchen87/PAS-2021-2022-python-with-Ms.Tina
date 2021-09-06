def add(a, b):
    print("ADDING %d + %d" % (a, b))
    return a + b + 1

def subtract(a, b):
    print("SUBTRACTING %d - %d" % (a, b))
    return a - b - 10

def multiply(a, b):
    print("MULTIPLYING %d * %d" % (a, b))
    return a*b*a

def divide(a, b):
    print("DIVIDING %d / %d" % (a,b))
    return a/2*b

print("Let's do some matn with just functions!")

age = add(30, 5)
height = subtract(78,4)
weight = multiply(90, 2)
iq = divide(100, 2)

def hi(a, b):
    return a + b

# 5^2
# multiply(x, x)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))

what = add(age, subtract(height, multiply(weight, divide(iq,2))))
what = divide(iq,2)
what = multiply(weight, what)
what = subtract(height, what)
what = add(age, what)

print("That becomes: ", what, "Can you do it by hand?")
class Animal(object):
    pass
# is a 
class Dog(Animal):
    # has a 
    def __init__(self, name):
        self.name = name

# is a 
class Cat(Animal):
    # is a 
    def __init__(self, name):
        # has a 
        self.name = name

# is a 
class Person(object):
    # is a 
    def __init__(self, name):
        # has a 
        self.name = name
        # has a 
        self.pet = None

# is a 
class Employee(Person):
    # is a
    def __init__(self, name, salary):
        # has a 
        super(Employee, self).__init__(name)
        # has a 
        self.salary = salary

# is a 
class Fish(object):
    pass
# is a 
class Salmon(Fish):
    pass
# is a
class Halibut(Fish):
    pass

# is a 
rover = Dog("Rover")
# is a 
satan = Cat("Satan")
# is a
mary = Person("Marry")
# is a 
mary.pet = satan
# is a 
frank = Employee("Frank",120000)
# has a 
frank.pet = rover
# is a 
flipper = Fish()
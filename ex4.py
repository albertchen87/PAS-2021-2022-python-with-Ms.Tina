# assign rick as a int var
rick=70
print("rick is " + str(rick) + "kg")

# assign car a int of 100
cars = 100
# assign sapce_in_a_car a float of 4.0
space_in_a_car = 4.0
# assign dirvers a int of 30
drivers = 30
# assign passengers a int of 90
passengers = 90
# assign cars_not_driven as cars - drivers
cars_not_driven = cars - drivers
# assign cars_driven as drivers
cars_driven = drivers
# assign carpool_capacity cars_driven*space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
#assign average_passengers_per_car passengers / cars_driven
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

'''
have put one extra _ between car and pool which you don't need
1. will not have the .0, it will not affect because now is dealing with int
2. can have decimals and not just integers
4. = is assign that thing a thing
5. ok
6.  i=1
    x=0
    j=i+x
    print(j)
'''
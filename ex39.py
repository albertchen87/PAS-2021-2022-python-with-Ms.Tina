states = {
    'Hsinchu': 'HS',
    'Taipei': 'TPE',
    'Taichung': 'TXG',
    'New York': 'NY',
    'Michigan': 'MI'\
}

cities = {'CA': 'San Francisco', 
'MI': 'Detroit',
'FL': 'Jacksonville'}

cities['NY'] = "New York"
cities['OR'] = "Portland"
cities['HS'] = "Hsinchu"
cities['TPE'] = "Taipei"
cities['TXG'] = "Taichung"

print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

print('-' * 10)
print("Michigan's abbreviation is : ", states['Michigan'])
print("Florida's abberviation is: ", states['Florida'])

print("-" * 10)
for state, abberv in states.items():
    print("%s is abberviated %s" % (state, abberv))

print("-" * 10)
for abberv, city in cities.items():
    print("%s has the city %s" % (abberv, city))

print("-" * 10)
state = states.get("Texas", None)

if not state:
    print("Sorry, no Texas.")
 
city = cities.get("TX", "Does Not Exist")
print("The city for the state 'TX' is: %s" % city)
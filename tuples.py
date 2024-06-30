# importing named tuple from collections library
from collections import namedtuple

# using a named tuple
Person = namedtuple('Person', "name age country")

# creating a named tuple
P1 = Person("Sunil", 21, "Nepal")

# accessing elements using property_name
print("Name: ", P1.name)
print("Age: ", P1.age)
print("Country: ", P1.country)

# Output
# Name:  Sunil
# Age:  21
# Country:  Nepal

# accessing using keywoard arguements
P2 = Person (name = "Khosta", age = 25, country= "Nepal")
print(P2)

# Output
# Person(name='Khosta', age=25, country='Nepal')
#Name: Nailah Wanjiku
#Date: 18/2/2026
#Program to show dictionaries in python

car = {"Model" : "Audi", "Make" : "Q8", "color":"cherry","Year" : 2025}

print(car)

print(car["Model"])
print(car["Year"])

students = {"Alice" : 24, "James" : 18, "Mark" : 22, "Daisy" : 19}

for key in students:
    print(key)

for val in students.values():
    print(val)
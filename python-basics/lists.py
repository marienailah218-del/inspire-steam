#Name: Nailah Wanjiku
#Date: 18/2/2026
#Program to show lists in python

#list of friends
friends = ["Rachel","Phoebe","Rose","Chandler","Monica","Joey"]

print(friends)
friends.sort()
print(friends)

friends.reverse()
print(friends)

friends.append("Jack")
print(friends)

new_friends = ["Sophy","Doris","Kade","Scott","Nelius"]

print(len(new_friends))

#new list of students
students = friends + new_friends
print(students)

students.pop()
print(students)

students.insert(5,"Vivian")
print(students)

students.insert(9, "Vallary")
print(students)

students.extend("Eve")
print(students)

students.remove("Vivian")
print(students)

new_students = students.copy()
print(new_students)
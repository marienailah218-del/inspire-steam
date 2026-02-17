#Name: Nailah Wanjiku
#Date: 16/2/2026
#Program to show if else conditions

age = int(input("enter your age :"))
height = (input("enter your height"))

if age >= 18:
    print("you are allowed to drive")
elif age < 18:
    print("you are too young to drive")


if age > 18 and height > 1.5 :
    print("you can play basketball")
elif age > 18 and height < 1.5:
    print("you can play rugby")
    

#Name: Nailah Wanjiku
#Date: 14/2/2026
#Program to calculate geometric progression


a = int(input("Enter the first number :"))
n = int(input("Enter the number of terms :"))
r = int(input("Enter the common ratio :"))

sn_gp = (a * (r**n)) / (r - 1)
print(f"The sum of the terms is : {sn_gp}")
#Name: Nailah Wanjiku
#Date: 13/2/2026
#Program to calculate arithmetic progression

#calculating nth term

a = int(input("enter the first number :"))
n = int(input("enter the number of terms :"))
d = int(input("enter the common difference"))

nth_term = a + (n-a) * d
sn = (n/2) *(2*a) +(n-1) *d


print(f"The nth term is : {nth_term}")



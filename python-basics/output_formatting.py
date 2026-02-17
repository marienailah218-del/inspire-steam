#Name: Nailah Wanjiku
#Date: 17/2/2026
#Program to format the output in different styles

name = "Nailah Marie"#name
weight = "50" #weight in kgs
fav_sport = "table tennis"
height = "160" #height in cms

# 1.format using print(f"{}")

print(f"My name is {name} and i weigh {weight} kgs")

# 2.using f string
text = f"my name is {name} and i love {fav_sport}"

print(text)

# 3.using {} and .format()

print("my name {0} and i am {1} cms tall".format(name,height))

# 4.using output specifiers %s -strings %f - float

import math
print('The value of pi is approximately %5.3f.'%math.pi)
print("i love %s " %fav_sport)
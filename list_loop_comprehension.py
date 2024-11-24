# Looping using list comprehension
#List comprehension offers the shortest syntax for looping through lists:
# fruits = ["apple", "mango","cherry"]
# [print(x) for x in fruits]


# [print(y) for y in ["bananas", "guavas", "laquats"] ]


#Based on a list of fruits, you want a new list, 
#containing only the fruits with the letter "a" in the name

v = ["apple", "banana", "cherry", "kiwi", "mango"]
v = []

for i in v:
    if "a" in i:
        v.append(i)

print(v)



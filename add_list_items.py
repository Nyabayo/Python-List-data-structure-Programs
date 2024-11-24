# Add list items
#Append items using append() method
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

#Insert items
# insert() method is used to insert elements at a specified index
m = ["melon", "orange", "mango"]
m.insert(2, "cherry")
print(m) # ["melon", "orange", "cherry", mango"]

# Extend list
# extend() method is used to append elements from another list to the current list
curr = ["mango", "pineapple", "papaya"]
typo = ["melon", "orange", "mango"]
curr.extend(typo)
print(curr)

# Add any Iterable
# The extend() method does not have to append lists, you can add any iterable
# object (tuples, sets, dictionaries etc.).
mylist =["apple", "banana", "cherry"]
mytuple = ("kiwi", "orange")
mylist.extend(mytuple)
print(mylist)
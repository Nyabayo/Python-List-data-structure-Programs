# Remove Specified Item
# The remove() method removes the specified item.
my = ["apple", "banana", "cherry"]
my.remove("apple")
print(my)

# If there are more than one item with the specified value, the remove() method removes the first occurrence:
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#Remove Specific Index
#The pop() method removes a specific index
mine = [7, 89, 4, 57, 0]
mine.pop(3)
print(mine)
# If you do not specify the index, the pop() method removes the last item.
r = [45, 87, 0]
r.pop()
print(r)

# The del keyword also removes the specified index:
x = ["apple", "banana", "cherry"]
del x[2]
print(x)
# The del keyword can also delete the list completely.
con = [34, 89, 30, 0]
print(con)
del con   # NameError: name 'con' is not defined
# print(con)  


# Clear the List

# The clear() method empties the list.

# The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

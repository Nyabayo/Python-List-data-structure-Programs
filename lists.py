#lists are used to store multiple items in a single variable
myList = ["chemestry", "biology", 23, "kiswahili"]
print(myList)

#LIst items are ordered, changeable, and allow duplicate values.
#define order, if you add an item it will be put at the end of the list
#Changeable we can change, add, and remove items
#Allow duplicates

#List Length: len
mine = ["she", "lin", "scv"]
print(len(mine))

#list()   :  constructor
my = list(("chipo", "cake", "samaki"))
print(my)

#Access list items : also negative indexing.
my_list = [23, 85, 8, 0, 7]
print(my_list[-1])

#Range of indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #cherry - kiwi

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-5:-2]) #cherry - kiwi

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) #cherry - mango
print(thislist[-4:-1]) # orange - melon
print(thislist[-6:-3]) # banana,orange

# Change List Items
fruits = ["orange", "cherry", "apple"]
# fruits[-1] = "banana"
# print(fruits)

#Change a Range o item values
fruits[0:1] = ["blackcurrant", "watermelon"] # ["blackcurrant", "watermelon", "cherry"apple"]
print(fruits)

x = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
x[2:5] = ["berry", "melon"] # ["apple", "banana","berry", "melon", "mango"]
print(x)
#replacing two values in one index
#Change the second value by replacing it with two new values:
y = ["apple", "banana", "cherry"]
y[1:2] = ["blackcurrant", "watermelon"]
print(y) # ["apple", "blackcurrant", "watermelon", "cherry"  ]

#Change the second and third value by replacing it with one value:
v = ["orange", "kiwi", "mango"]
v[1:3] = ["cherry"]
print(v) # ["orange", "cherry"]

#Insert items without replacing any  of the existing values
min = ["apple", "banana", "cherry"]
min.insert(-2, "melon")
print(min)

#Data type
f = [("banana", "cherry", 45)]
print(type(f))



# Loop Through a list
#you can loop through a list using for loop
mylist = ["apple", "banana", "cherry"]
for x in mylist:
    print(x)

# Loop Through the Index Numbers

# You can also loop through the list items by referring to their index number.

# Use the range() and len() functions to create a suitable iterable.
fruits = ["orange", "melon", "berry"]
for i in range(len(fruits)):
    print(fruits[i])

ladies = ["Favour", "Linet", "Maggy"]
for p in range(len(ladies)):
    print(f"index {p} : {ladies[p]}")

my_list = ["Python", "Java", "C++", "JavaScript", "Ruby"]

#  Using range(len())
print("Looping using range(len()):")
for i in range(len(my_list)):
    print(f"Index {i}: {my_list[i]}")

# Loop using index numbers
epl = ["Manchester City", "Chelsea", "Manchester United", "Arsenal", "liverpool"]
for o in range(len(epl)):
    print(f" {o} : {epl[o]}")




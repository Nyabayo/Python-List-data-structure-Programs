#Using while loop
# You can loop through list items using while loop
#Us the len() methon to determine the length of the list, 
#then start from 0 and loop your way through the list items by referring to their indexes
#remember to increase the index by one after each iteration

fruits = ["apple", "banana", "cherry"]
i = 0
while i < len(fruits):
    print(f"index {i} : {fruits[i]}")
    i = i + 1

countries = ["Kenya", "Uganda", "Tanzania", "Burundi"]
x = 0
while x < len(countries):
    # print(countries) without indexing
    print(countries[x])
    print(f"{x} : {countries[x]}")
    x = x + 1

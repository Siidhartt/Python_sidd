# itterable = an object/collection that can returnits elements one at a time,
#               allowing it to be iterated over in a loop



## LIST
numbers = [1 ,2, 3, 4, 5]

for num in reversed(numbers):
    print(num)

## SETS
fruits ={"apple" , "orange", "banana"}

for fruit in fruits :
    print(fruit)
#sets are not reversible

##STRINGS

name = "siddharth singh"
for character in name:
    print(character)

##DICTIONARY

my_dict = {"a":1, "b":2 , "c":3}

#if we itirate over a dictionary only the keys would get itirated
for x in my_dict:
    print(x) # this will return only the keys
#to itirate values 
for y in my_dict.values():
    print(y)
#to itirate both the keys and values

for x , y in my_dict.items():
    print(f"{x} = {y}")
# dictionary =  a collection of {key:value} pairs , it must contain key:value pairs
#                        ordered and changeable. No duplicates


capitals = {"USA":"Washington D.C.",
            "India":"New delhi",
            "China":"Beijing",
            "Russia":"Moscow"}


print(capitals.get("USA")) # this will return the key's value ie washington dc

#We can insert keys or update values of existing keys 
capitals.update({"Germany":"Berlin"}) 
capitals.update({"USA": "Detroit"})

print(capitals.get("USA")) #this will return detroit

# to clear the dictionary
#capitals.clear()

#to get all the keys [not their values]
keys = capitals.keys()
print(keys)

#we can itirate it using for loops too 
for key in keys:
    print(key)

# to get all the values in the dictionary [not the keys]
values = capitals.values() #we can itirate it too

#items method >>> returns a dictionary object which resembles a 2d list of tuples 
items = capitals.items()
print(items)
#USAGE

for key2,value2 in capitals.items():   #TO READ -- for every key2 value2  print every key value pair
    print(f"{key2}:{value2}")















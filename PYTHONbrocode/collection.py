#collection = single "variable" used to store multiple values 

# LIST = [] ordered and changeable. DUPLICATES OK
# SET =  {} unordered and immutable , but ADD/REMOVE OK . NO duplicates
# TUPLE= () ordered and unchangeable. DUPLICATES OK. FASTER



fruits = ["apple", "orange", "banana", "watermelon" , "coconut"]

#1.) LIST >>> [] ordered and changeable. DUPLICATES OK

#To access one of the elements in the list we can use INDEX operator 

print (fruits[3]) #this will print watermelon

print (fruits[0:2]) #this will print [apple , orange]

print (fruits[::2]) # this will print every second element begining with 0 i.e.  [apple , banana , coconut]  
print (fruits[::-1]) # this will REVERSE the list i.e. [coconut , watermelon , banana , orange , apple]  

#We can use for loop to ittirate over our collections    # COVENTION-- use the plural to assign the collection and singular to assign the counter for for_loop
for fruit in fruits:   #our counter(friut) is storing wtv values are within our collection(fruits)
    print(fruit)


#To get help with a collection
'''
print(dir(fruits))   #will give us all the attributes we can use with the collection
print(help(fruits))  #to get help with on how to use the attributes
'''

#length function 
print(len(fruits))


#in operator --- to find if a value is within out collection
print("apple" in fruits)  # this will return a boolean ie TRUE/FALSE

#With lists they are ordered and changeable ie we can change our list values even after we create it 
fruits[3] = "pineapple"  #using an index we can reassign the values [NOTE] the indexing parameter should be within the list range (here -- 4)


#append attribute --- to append a value at LAST of the list
fruits.append("mango")


#remove attribute ---  to remove a value from the list
fruits.remove("apple")


#insert attribute ---  to insert a value at any point of the list
fruits.insert(0,"kiwi")  #different from indexing a value since its not reassigning a value rather inserting it in the list


#sort attribute --- to sort a list in alphabetical order 
fruits.sort()


#reverse attribute --- to reverse our list
fruits.reverse()
print(fruits)


#index attribute --- to return us the index of the value present in the list
print(fruits.index("kiwi")) 

#count attribute --- to count the number of times a value is present in the list
print(fruits.count("banana"))


#clear attribute --- to clear a list
#fruits.clear()

#-----------------------------------------------------------------------------------------------------------------------------------------------------

#2.) Set >>> unordered and immutable , but ADD/REMOVE OK . NO duplicates

cars = {"toyota" , "honda" , "bmw" , "porsche"}
print(cars) #this will be unordered since sets are unordered

#length function  #to find the length of the collection
print(len(cars))


#in operator --- to find if a value is within our collection
print("mercedes" in cars)  # this will return a boolean ie TRUE/FALSE

#indexing in set is NOT POSSIBLE since sets are unordered 
#print(cars[0])              THIS WILL RETURN AN ERROR 


#we cannot change values in a set but can add/remove them
cars.add("ferrari")
cars.remove("bmw")
print(cars)

#pop attribute --- to remove the first element of the set BUT ITS GONNA BE RANDOM THO
fruits.pop()

#clear attribute --- to clear a set
#fruits.clear()

#----------------------------------------------------------------------------------------------------------------------------------------

#3.) TUPLE >>> ordered and unchangeable. DUPLICATES OK. FASTER

colors = ("blue" , "blue" , "red")

#same as others use

'''
print(dir(colors))   #will give us all the attributes we can use with the collection
print(help(colors))  #to get help with on how to use the attributes
'''
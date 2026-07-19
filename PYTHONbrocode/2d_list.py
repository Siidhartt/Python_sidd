#A 2d list is a list made up of list

fruits = ["apple" , "orange", "banana", "coconut"]
vegetables = ["celery" , "tomato" , "onion"]
meats = ["chicken", "mutton"] 

groceries = [fruits , vegetables, meats]   
#OR
# groceries = [ ["apple" , "orange", "banana", "coconut"] , ["celery" , "tomato" , "onion"] , ["chicken", "mutton"] ]

print(groceries) #it works like a matrix with 0 ,1, 2 as its ROWs  
#like this
"""
["apple" , "orange", "banana", "coconut"]
["celery" , "tomato" ,"onion"           ]
["chicken", "mutton"                    ] 
"""

print(groceries[0]) # this will return us the fruits list as its in the first row

#to index specific element use [][] like coordinates {should be inside the range }

print(groceries[0][2]) #will return banana

#To itirate over a list use loops
for collection in groceries:
    print(collection)


#To even itirate over the all the elements found inside the list use nested loops
for collection in groceries:
    for food in collection:
        print(food ,end =" ") #we are using end = "" to end it with a blank space
    print() # to print the elements in a new line 
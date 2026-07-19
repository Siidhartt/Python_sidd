#object = a "bundle" of related attributes (variables) and methods (functions)
#                     Ex. phone , book , cup 
#                 You need a "class" to create many objects
#

# class = (blueprint) used to design the structire and layout of an object

class car:
    def __init__(self):  # CONSTRUCTOR :  we need this method in order to create an object
        pass


class car:
    def __init__(self,model,year,color,for_sale):

# [NOTE] #just imagine self as the instance variables we made (here car1,2) as car1 and car2 will call this constructor and use the attributes we specify with self.____
        
        
        self.model = model 
        self.year = year                                   #These are some attributes associated with the car
        self.color = color 
        self.for_sale  = for_sale #boolean

    def drive(self):
        print(f"Your drive the {self.model} ")

    def stop(self):
        print(f"Your stop the {self.model} ")


#these are objects of class car

car1 = car("porsche" , 2022,"maroon" , False)
# print(car1)  this will give us the memory address of this car1 object where its located
print(car1.model) #" . " accesses the attributes of the object  
print(car1.year)  
print(car1.color)
print(car1.for_sale) 


car2 = car("ferrari" , 2020 , "red" , True)
print(car2.model) 
print(car2.year) 
print(car2.color) 
print(car2.for_sale) 
print(car2.for_sale) 
print(car2.for_sale) 


#we can import another class into this file and create objects of this class in that file.

import bike 
#or 
from bike import Bike  #this will import only the class Bike from the bike.py file

bike = Bike("harley" , 2008 , "black" , False)
print(bike.model) 
print(bike.year) 
print(bike.color) 
print(bike.for_sale) 
print(bike.for_sale) 
print(bike.for_sale) 



car1.drive()  #this will call the drive method of the car class
car2.stop()   #this will call the stop method of the car class
bike.drive()  #this will call the drive method of the bike class
bike.stop()   #this will call the stop method of the bike class














































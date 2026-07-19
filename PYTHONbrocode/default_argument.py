#default argument = A default value for certain parameters default is used when 
#                   that argument is omitted make your functions more flexible, reduces # of arguments 
#    1. positional 2.default 3.keyword 4. arbitrary



def net_price(list_price,discount,tax):
    return list_price *(1-discount)* (1+tax)

print(net_price(500,0,0.05))

#we can make it more flexible
def net_price(list_price , discount = 0 , tax = 0.05): # we are giving them a default arguments
    
    return list_price *(1-discount)* (1+tax)  #discount and tax are in %


print(net_price(500)) #this would also work ,,, 
#the benefit here is we can still give it arguments
print(net_price(500,0.02,0.17))

##EXERCISE -- TIMER

import time
def count(start,end):
    for x in range(start,end+1):   #we will start and then incriment every 1 sec
        print(x)
        time.sleep(1) #to print the times every 1 sec just how a timer does
    print("DONE!!")

count(0 , 10) 

#using default arguments here 
import time

#def count(start=0,end): NOTE -- #THIS WILL RETURN AN ERROR SINCE DEFAULT ARGUMENTS SHOULD ALWAYS BE POSITIONED AFTER POSITIONAL ARGUMENTS
def count(end,start=0): 

    
    for x in range(start,end+1):   #we will start and then incriment every 1 sec
        print(x)
        time.sleep(1) #to print the times every 1 sec just how a timer does
    print("DONE!!")

count(7) 
#if we want to give it another starting point we can do it too
count(7,2)
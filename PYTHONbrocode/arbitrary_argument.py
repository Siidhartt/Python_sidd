# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword arguments

# * == unpacking operator
#used when we dont know how many arguments the user is gonna pass

# *ARGS :

def add (a ,b):
    return a+b

print(add(1,2))
#but print(add(1,2,3)) will return an error since we only defined 2 positional arguments 

#HERE WE CAN USE *args 

def add(*nums):   #Parameter args is a tuple
    total = 0        
    
    for num in nums:  #arg is just a naming convention we can use any name
        total += num 
    
    return total

print(add(1,3,4,5,6))

#Example --

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Er." , "siddharth","singh") #with the unpacking operator with a unique argument name (here: args) we can pack these arguments in a tuple


# **KWARGS :

def print_address(**kwargs):  #kwargs is a dictionary so we can use dictionary's parameters

#for values
    for value in kwargs.values():
        print(value)

#for keys
    for key in kwargs.keys():
        print(key)

#usage
    for key, value in kwargs.items():
        print(f"{key} : {value}")


print_address(street = "aklfdj" , 
              city = "varanasi", 
              state = "utar pradesh")


#EXAMPLE 

def shipping_label(*args,**kwargs): # args take positional arguments , kwargs take keyword arguments
    for arg in args:
        print(arg,end = " ")
    print()

    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('country')}")

shipping_label("Dr", "max", "gerrald", "III",
               street ="23rd jump street",
               city="varanasi",
               state="uttarpradesh",
               country = "india")


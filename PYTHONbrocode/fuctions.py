# function = A block of reusable code
            # place () after the function name to invoke it 


def happy_birthday():
    print("happy birthday")


happy_birthday() #we are CALLING the function



#We can send values or variables directly to a function called arguements
def name(self):
    print(f"my name is {self}")

name("siddharth")
name("krishna")

#We can put multiple number of arguemens
def city(city_name,pincode):
    print(f"I live in {city_name}")
    print(f"its pincode is {pincode}")

city("varanasi",221106)  #Parameter's order/position matters


#Funciton to display an invoice
def display_invoice(username , amount , due_date):
    print(f"Hello {username}")
    print(f"Your bill of ₹{amount} is due: {due_date}")

display_invoice("Sidd", 10200 , "01/09/2027")


#return = statement used to end a function and send a result back to the caller

def add(x,y):
    z = x+y
    return z
 
def subtract(x,y):
    z = x-y
    return z
 
def multiply(x,y):
    z = x*y
    return z
 
def divide(x,y):
    z = x/y
    return z 

print(add(1,4))
print(subtract(1,4))
print(multiply(1,4))
print(divide(1,4))


#Function to print the full name
def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last


full_name = create_name("siddharth","singh")
print(full_name)



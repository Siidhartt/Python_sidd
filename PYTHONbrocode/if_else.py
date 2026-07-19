# if = do somw code only if somw condition is True 
# else do something else 

#EXAMPLE 1 
age = int(input("enter your age : "))

if age >= 200:
    print("You are too old")

elif age >= 18:                     #To give conditions , there can be multiple elif
    
    print("You are eligible")

elif age < 0:                
    print("Enter valid age")

else:
    print("You must be 18+ to sign up")



#EXAMPLE 2:

response = input("Would u like some food? (Y/N) :")

if response== "Y":
    print("Have some food")

else:
    print("No food for you")


#EXAMPLE 3 [BOOLEAN WITH IF STATEMENTS]:

for_sale = False             #either write a condition of use a boolean
if for_sale:
    print("item for sale")
else:
    print("Not for sale")












item = input("What item do u want to buy : ")

price = float(input("What's its price : "))
quantity = int(input("How many would you like : "))

total =  price*quantity

print(f"Your total is : ₹{round(total)}")    #round is a function to round up the float/int value 
print (f"THANK YOU")
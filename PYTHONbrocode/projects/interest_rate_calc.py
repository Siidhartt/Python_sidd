import math


#specifying variables
principle = 0  
rate = 0
time = 0



while True:
    principle = float(input("Enter your principle amount : "))
    if principle < 0:
        print("principle cannot be less than zero")
    else:
        break


while True :
    rate = float(input("Enter your interest rate : "))
    if rate<0:
        print("rate cannot be less than zero")
    else:
        break


while time<=0:
    time = int(input("Enter your time in years : "))
    if time <= 0:
        print("time cannot be less than or equal to zero")
    
    



total_amount = principle * (pow(1 + rate /100,time))

print(f"Your total amount after {rate}% interest rate for {time} year(s) is {total_amount:.3f}" )
import time

#using while loops 
import time 
countdown_time= int(input("Enter the time for countdown in seconds: "))

while countdown_time > 0:
    
        seconds = countdown_time % 60  # so that the remainder stays below 60 just like in an actual clock
        minutes = int(countdown_time /60) % 60
        hours = int(countdown_time/3600)
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        countdown_time = countdown_time-1
        time.sleep(1)
print("Countdown over")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

#using for loops

countdown_time = int(input("Enter the time in seconds: "))

for x in range(countdown_time,0,-1):
    seconds = x % 60  # so that the remainder stays below 60 just like in an actual clock
    minutes = int(x /60) % 60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")

    time.sleep(1)
print("TIME'S UP")

#-------------------------------------------------------------------------------------------------------------------------------------------------
"""
countdown_time= int(input("Enter the time for countdown in seconds: "))


for x in reversed(range(0,countdown_time)): # to print the countdown in reverse
    print(x)
    time.sleep(1)
print("TIME'S UP")



#ANOTHER SYNTAX for printing in reverse
for x in range(countdown_time,0,-1): 
    print(x)
    time.sleep(1)
print("TIME'S UP") """

import math

radius = float(input("enter the radius of the circle: "))

Area1 = math.pi * radius**2

#OR 

Area2 = math.pi * pow(radius , 2)

print(f"The area of the circle is {round(Area2 , 2) }cm^2")  #it will round to 2 decimal places
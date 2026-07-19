#logical operators = conditional operators

"""    and = checks two or more conditions if True
       or = check if at least one codition is True 
       not = True if condition is False , and vice versa"""


temp = 20
sunny = False 

if temp <= 0 or temp >= 30:
    print("The temp is bad")
else:
    print("The temp is good ")

if temp >=0 and sunny ==True:
    print("You can go outside")
elif not sunny:
    print("It is cloudy outside")

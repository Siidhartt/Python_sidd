#conditional expression = a one line shortcut for the if-else statement (ternary operator)
#                       Print or assign one of two values based on a condition
#                       [SYNTAX] X if condition else Y >>>>>>>>> meaning = return x if "condition" is valid else return y

num = 6
a = 13
b = 10
age = 4
temperature = 30
user_role = "admin"


print("Positive" if num>0 else "negative") #or we can assign a variable to the whole statement SEE LINE 12

result = "Even" if num %2 == 0 else "ODD"
print (result)

max_num = a if a > b else b 
min_num = a if a<b else b
print(max_num)
print(min_num)


status = "You are an adult" if age>18 else "You are underage"
print(status)


weather = "hot" if temperature>20 else "cold"
print(weather)


access_level = "Full access" if user_role == "admin" else "Limited access"
print(access_level)
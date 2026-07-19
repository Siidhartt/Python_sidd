name = input("Enter Your Full Name : ")

# 1. 
result  = len(name)  # gives us the length of the string {output is an INTEGER}
#usage :
condition_name = "name is valid" if result<20 else "Try smaller name"
print(condition_name)

# 2.
result2 = name.find(" ")   #will find the FIRST occurence of a string at the letter's place (starts with 0 ) ( -1 if no occurence) {output is an INTEGER} 
#usage :
condition_space = "Valid name with no spaces" if result2 == -1 else "There shouldn't be any spaces in your name"
print (condition_space) 
#print(output)   this is just  to check where is the space occuring

# 3. 

result3 = name.rfind(" ") # r = reverse , will find the LAST occurence of a string at the letter's place {output is an INTEGER}

# 4.

name = name.capitalize()  #To capitalize the string (here) it will capitalize the first letter
print (name)

# 5. 
name = name.upper() #To make the string uppercase
print(name)

# 6. 
name = name.lower()

# 7.
result_with_onlydigits = name.isdigit() # returns True/False if the string ONLY contains digits or not {output is a BOOLEAN}
print(result_with_onlydigits)

# 8. 
result_with_onlyalphabets = name.isalpha()  # returns True/False if the string ONLY contains aplha or not {output is a BOOLEAN}
print(result_with_onlyalphabets)

# 9.
phonenumber = input("Enter Your Phone num : ")
output = phonenumber.count("-") #counts the number of string {output is an INTEGER}
print(output)

# 10.

output_replace = phonenumber.replace("-" , " ")  # Replaces the string with the given character
print(output_replace)



##### print(help(str))   to see all the possible methods we can use in string


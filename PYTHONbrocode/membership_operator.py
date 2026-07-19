# Membership operators = used to test whether a value or variable is found in a sequence
#                                             (string, list, tuple, set, or dictionary)
#                                             1. in -- will test to see if a value or a variable is found in the sequence
#                                             2. not in -- opposite of in 

word = "apple"

letter  = input("Guess the letter in the secret word: ")


if letter in word: # "in" / "not in" will return a boolean value ie True/False
    print(f"there is a {letter}")

elif letter not in word:
    print(f"{letter} was not found")



#EXAMPLE:

student = {"siddharth" , "krishna" , "max" , "jaskjjf"}


user_input = input("Enter the name of the student: ")


if user_input in student:
    print(f"{user_input} is present")

else:
    print(f"{user_input} not found")


#EXAMPLE:

grades = {"krishna":"A", 
          "siddharth":"A+" , 
          "max":"C-"}



student = input("Emter the name of the student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")

else:
    print(f"{student} was not found")


#EXAMPLE:

email = "hfashfolkas@gmail.com"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")




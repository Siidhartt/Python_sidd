#while loop = execute some code WHILE some condition remain true

#EXAMPLE 1

name = input("Enter Your Name: ")

while name == "":
    print("You didnt enter your name")
    name = input("Enter Your Name: ") #the input will be in a loop  ##if we done give it an input loop then line 7 will keep on repeating forever
 

print(f"Hello {name}") #this will be performed when the condition is not true{i.e if they enter  their name}


"""while this condition is true execute this code in line 7&8 until that condition is not true {line 11} potentially forever"""


#EXAMPLE 2 

food = input("Enter a food you like (q to quit): ")

while not food == "q":    # until the input is NOT q 
    print(f"You like {food}") 
    food = input("Enter a food you like (q to quit): ")
print("bye")
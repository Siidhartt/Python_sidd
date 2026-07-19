#generating random numbers
import random #never use this module for secret or encryption purpose [use the "secret" module for that]

low = 1
high = 70



ran_num = random.randint(low,high) #we are giving it a range [ 1 to 70 ] to print a random number 

# for random floating point number 
ran_num2 = random.random() #this wil return a random floating point number between 0 & 1  NOTE ---- random.random module doesnt take any arguements

#To return a random choice from provided options
options = ("rock", "paper", "scissors")
option = random.choice(options)
print(option)

#To shuffle the seq of any collection
cards = ["2" , "3" , "4","5", "AFHAKSHF"]
random.shuffle(cards)
print(cards)



#NUMBER GUESSING GAME 
import random
low = 1
high = 10

guesses = 0

random_number = random.randint(low,high)
#print(random_number)



while True :
    userinput = int(input(f"Enter your guessed Number between {low} and {high}: "))
    
    if userinput < random_number:
        print(f"{userinput} is too low")
        guesses += 1
    elif userinput > random_number:
        print(f"{userinput} is too high")
        guesses += 1
    elif userinput == random_number:
        print("Youre correct!!")
        break 
        
print(f"You took {guesses} ")


                        
        
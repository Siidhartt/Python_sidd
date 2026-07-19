#Python quiz game

questions = (("Formula of work done"),
             ("How many elements are in the periodic table"),
             ("What comes after helium "),
             ("Who wrote the trial"))
options = (("A) f=ma", "B) w=fs","C) r=uxT"),
           ("A) 113" ,"B) 112" ,"C) 118"),
           ("A) lithium","B) berylium","C) sodium"),
           ("A) julius ","B) kafka","C) shakespeare"))

#variables
score = 0
answers = ["B","C","A","B"]
guesses = [] #we are using list here since it will hold our answers and making changes is possible in it
question_num = 0


for question in questions:
    print("--------------------------------------------------------------------")
    print(question)
    
    for option in options[question_num]:
        print(option)
    
    guess = (input("Enter (A , B , C , D):").upper())
    guesses.append(guess)
    if guess == answers[question_num]:
        score+=1
        print("CORRECT!!")
    else:
        print("INCORRECT:(")
        print(f"Correct answer of Q{question_num+1} is {answers[question_num]}")
    
    question_num+=1    
print("--------------------------------------------------------------------")
print("       RESULT       ")
print(f"Guesses: {guesses}")
print(f"Answers: {answers}")

score = (score / len(questions)*100)
print(f"SCORE : {score}%")
import random

options = ("rock","paper","scissors")
player = None
player_score = 0
computer_score = 0


while True:
        computer = random.choice(options)
        player = input("Enter your choice (s to see score): ")
        
        
        if player.lower() == "s":
            break
        
        
        print(f"Player: {player}")
        print(f"Computer: {computer}")
        
        
        
        if player not in options:
            print("Enter a valid choice")
            
        elif player == computer :
            print("TIE")
            
        elif player == "rock" and computer == "paper":
            print("Player won")
            player_score += 1
            
        elif computer == "rock" and player == "paper":
            print("Computer won")
            computer_score += 1
            
        elif computer == "scissors" and player == "paper":
            print("Computer won") 
            computer_score += 1
            
        elif player == "scissors" and computer == "paper":
            print("Player won") 
            player_score += 1
            
        elif player == "rock" and computer == "scissors":
            print("Player won") 
            player_score += 1
            
        elif computer == "rock" and player == "scissors":
            print("Computer won") 
            computer_score += 1

        

print(f"SCORE: PLAYER: {player_score} ,, COMPUTER: {computer_score}")








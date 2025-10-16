import random

user_wins=0
computer_wins=0

options=["rock","paper","scissor"]

while True:
    user_input=input("Take rock/paper/scissor or Q to quit :  ").lower()
    
    if user_input=="q":
        break
    
    if user_input not in options:
        continue
    
    random_number=random.randint(0,2)
    
    # rock:0 , paper:1, scissor:2
    
    computer_picks=options[random_number]
    print("Computer picks ", computer_picks + ".")
    
    if user_input==computer_picks:
        print("It's a draw")
    
    elif user_input=="rock" and computer_picks=="scissor":
        print("You win! ")
        user_wins+=1
        
    elif user_input=="paper" and computer_picks=="rock":
        print("You win! ")
        user_wins+=1
        
    elif user_input=="scissor" and computer_picks=="paper":
        print("You win! ")
        user_wins+=1
        
    else:
        print("You Lost :)")
        computer_wins+=1
        
print("You won ", user_wins, "times ")

print("Computer wins",computer_wins, "times")


print("Good bye!  Have  a good day")        
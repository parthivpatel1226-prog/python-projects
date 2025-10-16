import random

#How bigger number user wants to genrate :

top_of_range=int(input("Type a number : "))


if top_of_range <=0:
    print("Please Enter a number greater than 0: ")
    quit()
    
else:
    print("Type a number : ")
    
random_number=random.randint(0,top_of_range)

guess=0

while True:
    guess+=1
    user_guess=int(input("Make a guess :"))
    
    
    if user_guess==random_number:
        print(" OH! that's great. You got it! ")
        break
    
    
    else:
        print("You got it wrong ")
        
        if user_guess > random_number:
            print("You are above the number ")
            
            
        else:
            print("You are below the number ")
            
            
print('You got it in',guess,'guesses')
print("Thank You for playing the game :) ")

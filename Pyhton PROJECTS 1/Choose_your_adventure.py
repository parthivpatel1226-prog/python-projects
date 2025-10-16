name=input("What's your name: ")
print("Welcome",name,"to this adventure :) ")

answer=input("You are on a dirt road. It has come to end and you can go left or right. Where you wanna go (left/right)").lower()

if answer=="left":
    
    answer=input("You came to a river. You can walk around or swim across. What do you want(walk/swim)").lower()
    
    if answer=="swim":
        print("You swam and eaten by an aligator.  You Lost :) ")
        
    elif answer=="walk":
        print("You walked for many miles , ran out of water and You lost the game. ")
    
    else:
        print("Not a valid option. You loose. ")
    
    
            
elif answer=="right":
    
    answer=input("You came to a bridge, It looks woobly, Do you want to cross it or wanna go back  (crosss/back):").lower()
    
    if answer=="back":
        print("You go back. You Lost the game :)")
        
    elif answer=="cross":
        answer=input("You crossed the bridge, And meet the strangers. Do you wanna talk to them (yes/no)").lower()
        
        if answer=="yes":
            print("You talked to the strangers. They gave you gold.   YOU WON the game ! :)")
            
        elif answer=="no":
            print("You ignored the strangers. They are offended.  You lost the game.")
            
        else:
            print("Not a valid option, You Lost")
    else:
        print("Not a valid option, You Lost")
        
else:
    print("Not a valid option, You Lost")
        
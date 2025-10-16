print("Welcome to my Quiz ! ")

playing=input("Do you want to play ?")

if playing.lower() != "yes":
    print("Thank You!")
    quit()
print("OK, Let's Play :)")

score=0

answer=input("What does GPU stands for?")
if answer.lower()=="graphics processing unit" :
    print("Correct!")
    score+=1
    
else:
    print("Incorrect")
    
answer=input("What does CPU stands for ?")
if answer.lower()=="central processing unit" :
    print("Correct!")
    score+=1

else:
    print("Incorrect")
    
answer=input("What does GUI stands for?")
if answer.lower()=="graphical user interface":
    print("Correct!")
    score+=1
else:
    print("Incorrect")
    
answer=input("[12−(3×2)]×(4+2)=?")
if answer=="36":
    print("Corect!")
    score+=1
else:
    print("Incorrect")
    


print("You got"  +str (score)+  "questions correct")
print("You got"  +str ((score/4)*100)+ "%")

    
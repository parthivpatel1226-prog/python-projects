from cryptography.fernet import Fernet

master_pwd= ("What is the masrter password :")


def write_key():
    key = Fernet.generate_key()
    with open ("key.key", "wb") as key_file:
        key_file.write(key)
    
write_key()   


def load_key():
    file= open("key.key" , "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)

def view():
    with open("pass.txt","r") as f:
        for line in f.readlines():
            data= line.rstrip()
            user , passw = data.split("|")
            print("User :",  user , "| Password:", fer.decrypt(passw.encode()).decode())
            
            
                
            
def add():
    name= input('Account name : ')
    pwd=input("Password :")
    
    with open("pass.txt" , "a") as f :
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
        
        
        
while True:
    mode= input(" Would you like to add a new password or wanna view existing ones (view/add/quit)").lower()
    
    if mode=="q":
        break
    elif mode=="view":
        view()
        
    elif mode == "add":
        add()
        
    else:
        print("Invalid Mode :")
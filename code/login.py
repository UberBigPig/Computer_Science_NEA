#Login system
import files as file
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


#load files
accountLogin = file.load("accountLogin")



#create an account
def createAccount(username, password, confirmPassword):
    #check if details are valid
    if checkUsername(username) == True and checkPassword(password) == True and checkPasswordMatch(password, confirmPassword):
        #save to file
        accountLogin.append([username, password])
        file.save(accountLogin, "accountLogin")
    else:
        return False

#check if username is valid
def checkUsername(username):
    for i in range(0, len(accountLogin)):
        if accountLogin[i][0] == username:
            return False
    return True


#check if password is valid
def checkPassword(password):
    SpecialSym = ["$", "@", "#", "%", "&", "!", "£", "*", "/", "?"]
    checkResult = True
    
    # Check length
    if len(password) < 6:
        checkResult = False
        ("print too short")
            
    if len(password) > 20:
        checkResult = False
        print("too long")
    
    # Check for digits
    if not any(char.isdigit() for char in password):
        checkResult = False
        print("no digit")
    
    # Check for uppercase letters
    if not any(char.isupper() for char in password):
        checkResult = False
        print("no upper case")
    
    # Check for lowercase letters
    if not any(char.islower() for char in password):
        checkResult = False
        print("no lower case")
    
    # Check for special symbols
    if not any(char in SpecialSym for char in password):
       checkResult = False
       print("no special char")


    return checkResult

def checkPasswordMatch(password, confirmPassword):
    if password == confirmPassword:
        return True
    else: 
        return False

#Check if log in info is valid
def login(username, password):
    for i in range(0, len(accountLogin)):
        if username == accountLogin[i][0]:
            if password == accountLogin[i][1]:
                print("Logged in successfully!")
                return True
    return False


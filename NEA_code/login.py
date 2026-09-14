#Login system
import files as file
import ttkbootstrap as ttk
import tkinter as tk

#load files
accountLogin = file.load("accountLogin")

print(len(accountLogin))

#create an account
def createAccount(username, password):
    #check if details are valid
    if checkUsername(username) == True and checkPassword(password) == True:
        #save to file
        accountLogin.append([username, password])
        file.save(accountLogin, "accountLogin")
    elif checkUsername(username) == False:
        print("Username Error")
    elif checkPassword(password) == False:
        print("Password Error")

#check if username is valid
def checkUsername(username):
    for i in range(0, len(accountLogin)):
        if accountLogin[i][0] == username:
            return  False
    return True


#check if password is valid
def checkPassword(password):
    SpecialSym = ["$", "@", "#", "%", "&", "!", "£", "*", "/", "?"]
    checkResult = True

    # Check length
    if len(password) < 6:
        print('Length should be at least 6')
        checkResult = False
        
    if len(password) > 20:
        print('Length should not be greater than 20')
        checkResult = False

    # Check for digits
    if not any(char.isdigit() for char in password):
        print('Password should have at least one numeral')
        checkResult = False

    # Check for uppercase letters
    if not any(char.isupper() for char in password):
        print('Password should have at least one uppercase letter')
        checkResult = False

    # Check for lowercase letters
    if not any(char.islower() for char in password):
        print('Password should have at least one lowercase letter')
        checkResult = False

    # Check for special symbols
    if not any(char in SpecialSym for char in password):
        print('Password should have at least one of the symbols $@#%')
        checkResult = False

    return checkResult

#Login to an account
def login(username, password):
    for i in range(0, len(accountLogin)):
        if username == accountLogin[i][0]:
            if password == accountLogin[i][1]:
                return True
    return False

createAccount("username", "Pa$$w0RD")

#create GUI

loginW = ttk.Window(size=(300, 200))

labelFrame = ttk.Labelframe(loginW, text= "Login").pack(expand= True, fill= "both")
button = ttk.Button(labelFrame, text= "Button").pack()




loginW.mainloop()









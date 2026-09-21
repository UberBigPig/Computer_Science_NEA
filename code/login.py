#Login system
import files as file
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


#load files
accountLogin = file.load("accountLogin")

print(len(accountLogin))

#create an account
def createAccount(username, password, confirmPassword):
    #check if details are valid
    if checkUsername(username) == True and checkPassword(password, confirmPassword) == True:
        #save to file
        accountLogin.append([username, password])
        file.save(accountLogin, "accountLogin")
    elif checkUsername(username) == False:
        print("Username Error")
    elif checkPassword(password, confirmPassword) == False:
        print("Password Error")

#check if username is valid
def checkUsername(username):
    for i in range(0, len(accountLogin)):
        if accountLogin[i][0] == username:
            infoWindow("Username already exists")
            return  False
    return True


#check if password is valid
def checkPassword(password, confirmPassword):
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

    if password != confirmPassword:
        infoWindow("Passwords do not match")
        checkResult = False

    if checkResult == False:
        infoWindow("Password must have: \n-between 6 and 20 characters\n-at least one uppercase letter\n-at least one number\n-at least one special symbol")
        print("password does not meet requriements")
    return checkResult

#Check if log in info is valid
def login(username, password):
    for i in range(0, len(accountLogin)):
        if username == accountLogin[i][0]:
            if password == accountLogin[i][1]:
                print("Logged in successfully!")
                return True
            infoWindow("Incorrect password")
        infoWindow("Username does not exist")
    return False

#create window to show info (e.g. incorrect password)
def infoWindow(error):
    infoWindow = ttk.Window()

    photo = ttk.PhotoImage(file="resources/warning.png")
    label = ttk.Label(infoWindow, image=photo)
    label.image = photo          
    label.pack(padx=20, pady=20, side=LEFT)


    ttk.Label(infoWindow, text=error).pack(padx=15, pady=30, side=RIGHT)


    infoWindow.mainloop()

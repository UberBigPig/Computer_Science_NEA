import login
import ttkbootstrap as ttk
from ttkbootstrap.constants import *





#function to clear the widgets out of a frame
def clearFrame(frame):
    for widget in frame.winfo_children():
        widget.pack_forget()

#create window
def loginWindow():
    global window
    window = ttk.Window()
    firstMenu(window)






    window.mainloop()

#create the menu that is shown first
def firstMenu(window):
    clearFrame(window)

    loginUsername = ttk.StringVar()
    loginPassword = ttk.StringVar()

    createUsername = ttk.StringVar()
    createPassword = ttk.StringVar()
    confirmPassword = ttk.StringVar()

    content = ttk.Frame(window)
    content.pack(fill=BOTH, expand=True, padx=10, pady=20)

    # login section
    loginLabelFrame = ttk.Labelframe(content, text="Sign in")
    loginLabelFrame.pack(side=LEFT, fill=Y, expand=True, padx=(0, 10))

    #input for username
    ttk.Label(loginLabelFrame, text="Username").pack()
    ttk.Entry(loginLabelFrame, bootstyle=PRIMARY, textvariable= loginUsername).pack(padx=10, pady=10)

    #input for password
    ttk.Label(loginLabelFrame, text="Password").pack()
    ttk.Entry(loginLabelFrame, bootstyle= PRIMARY, textvariable=loginPassword, show="*").pack(padx=10, pady=10)


    #Button
    ttk.Button(loginLabelFrame, text="Log in", bootstyle= PRIMARY, command=lambda: loginButton(loginUsername.get(), loginPassword.get(), loginLabelFrame)).pack(padx=10, pady=10, fill=X)



    # separates both parts
    ttk.Separator(content, orient=VERTICAL, bootstyle=PRIMARY).pack(side=LEFT, fill=Y, pady=10)



    #create account section
    createLabelFrame = ttk.Labelframe(content, text="Create account")
    createLabelFrame.pack(side=LEFT, fill=Y, expand=True, padx=(10, 0))

    #input for username
    ttk.Label(createLabelFrame, text="Username").pack()
    ttk.Entry(createLabelFrame, bootstyle=PRIMARY, textvariable=createUsername).pack(padx=10, pady=10)

    #input for password
    ttk.Label(createLabelFrame, text="Password").pack()
    ttk.Entry(createLabelFrame, bootstyle= PRIMARY, textvariable=createPassword, show="*").pack(padx=10, pady=10)

    ttk.Label(createLabelFrame, text="Confirm Password").pack()
    ttk.Entry(createLabelFrame, bootstyle=PRIMARY, textvariable=confirmPassword, show="*").pack(padx=10, pady=10)

    #Button
    ttk.Button(createLabelFrame, text="Create account", bootstyle= PRIMARY, command=lambda: createButton(createUsername.get(), createPassword.get(), confirmPassword.get())).pack(padx=10, pady=10, fill=X)



#function that is called when log in button is pressed
def loginButton(username, password, frame):
    if login.login(username, password) == True:
        print("Logged in")
        return True
    else:
        errorWidget("Wrong username or password", frame)
        return False




#function that is called when the create account button is pressed
def createButton(username, password, confirmPassword):
    login.createAccount(username, password, confirmPassword)


#widget to replace a frame with an error message
def errorWidget(error, frame):
    clearFrame(frame)
    photo = ttk.PhotoImage(file="resources/warning.png")
    label = ttk.Label(frame, image=photo)
    label.image = photo          
    label.pack(padx=20, pady=20)
    ttk.Label(frame, text=error).pack(padx=15, pady=30)
    ttk.Button(frame, text="Back", command=reset).pack()


def reset():
    firstMenu(window)

loginWindow()











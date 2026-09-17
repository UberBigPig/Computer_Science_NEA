import login
import ttkbootstrap as ttk
from ttkbootstrap.constants import *





#function to clear the widgets out of a frame
def clearFrame(frame):
    for widget in frame.winfo_children():
        widget.pack_forget()

#create window
def loginWindow():
    window = ttk.Window()
    firstMenu(window)






    window.mainloop()

#create the menu that is shown first
def firstMenu(window):

    loginUsername = ttk.StringVar()
    loginPassword = ttk.StringVar()

    createUsername = ttk.StringVar()
    createPassword = ttk.StringVar()




    content = ttk.Frame(window)
    content.pack(fill=BOTH, expand=True, padx=10, pady=20)

    # login section
    loginLabelFrame = ttk.Labelframe(content, text="Sign in")
    loginLabelFrame.pack(side=LEFT, fill=Y, expand=True, padx=(0, 10))

    #input for username
    ttk.Entry(loginLabelFrame, bootstyle=PRIMARY, textvariable= loginUsername).pack(padx=10, pady=10)

    #input for password
    ttk.Entry(loginLabelFrame, bootstyle= PRIMARY, textvariable=loginPassword, show="*").pack(padx=10, pady=10)

    #Button
    ttk.Button(loginLabelFrame, text="Log in", bootstyle= PRIMARY).pack(padx=10, pady=10, fill=X)


    # separates both parts
    ttk.Separator(content, orient=VERTICAL, bootstyle=PRIMARY).pack(side=LEFT, fill=Y, pady=10)



    #create account section
    createLabelFrame = ttk.Labelframe(content, text="Create account")
    createLabelFrame.pack(side=LEFT, fill=Y, expand=True, padx=(10, 0))

    #input for username
    ttk.Entry(createLabelFrame, bootstyle=PRIMARY, textvariable=createUsername).pack(padx=10, pady=10)

    #input for password
    ttk.Entry(createLabelFrame, bootstyle= PRIMARY, textvariable=createPassword, show="*").pack(padx=10, pady=10)

    #Button
    ttk.Button(createLabelFrame, text="Create account", bootstyle= PRIMARY).pack(padx=10, pady=10, fill=X)

loginWindow()
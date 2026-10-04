import ttkbootstrap as ttk
import files as file
import login
from ttkbootstrap.constants import *

def getUsername(currentUser):
    global username 
    username = currentUser
    



global settings
settings = file.load("settings")
global userTheme
global userMode
userTheme = "bootstrap"
userMode = "light"
for i in range(len(settings)):
    if settings[i][0] == username:
        userTheme = settings[i][1]
        userMode = settings[i][2]
    else:
        userTheme = "bootstrap"
        usermode = "light"


#create window for GUI widgets
class climbingTracker(ttk.Window):
    def __init__(self):
        #can also add icon if necessary
        super().__init__(title= "Climbing Tracker", size=(600, 500), iconphoto="resources/logo.png")
        self.theme_use(f"{userTheme}-{userMode}")
        #create sidebar and buttons on left
        #pageFrame(self)

        #create frame for content that will change
        self.contentFrame = ttk.Frame(self).pack(side=RIGHT, expand=True, fill=BOTH)

    def createSidebar(self):
        pageFrame(self)

    def applySettings(self, theme, dark):
        print(dark.get())
        mode = ""
        if dark.get() == False:
            mode = "light"
        elif dark.get() == True: 
            mode = "dark"
        print(mode)
        useTheme = theme.get()
        self.theme_use(f"{useTheme}-{mode}")
        print(dark.get()) 
        file.save([username, useTheme, mode])


    #function to clear frame with changing content
    def clearFrame(self):
        for widget in self.contentFrame.winfo_children():
            widget.destroy()

    ###functions to display pages

    #display global leaderboard
    def openGlobalLeaderboard(self):
        self.clearFrame()
        GLFrame(self)

    def openHome(self):
        self.clearFrame()
        home(self)

    def openPrivateLeaderboard(self):
        self.clearFrame()
        PLFrame(self)

    def openUserStats(self):
        self.clearFrame()
        userStats(self)

    def openSettings(self):
        self.clearFrame()
        settings(self)


#create sidebar
class pageFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(side=LEFT, fill="y", pady=5, padx=5)

        #add seperator for aesthetic purposes
        ttk.Separator(self, orient=VERTICAL).pack(side=RIGHT, fill=Y, pady=10)

        #button for home menu
        ttk.Button(self, icon="house-fill", text="Home", command=master.openHome).pack(fill=BOTH, pady=5, padx=5)

        #button for global leaderboard
        ttk.Button(self, icon="globe-americas-fill", text="Global Leaderboard", command=master.openGlobalLeaderboard).pack(fill=BOTH, pady=5, padx=5)

        #button for private leaderboard
        ttk.Button(self, icon="people-fill", text="Private Leaderboard", command=master.openPrivateLeaderboard).pack(fill=BOTH, pady=5, padx=5)

        #button for user stats
        ttk.Button(self, icon="graph-up", text="User Statistics", command=master.openUserStats).pack(fill=BOTH, pady=5, padx=5)

        #button for settings
        ttk.Button(self, icon="gear-fill", text="Settings", command=master.openSettings).pack(fill=BOTH, pady=5, padx=5)

        #add more buttons here:


#create frame for home page (to log activity and see personal stats etc.)
class home(ttk.Labelframe):
    def __init__(self, master):
        super().__init__(master.contentFrame, text="Home")
        self.pack(side = RIGHT, expand=True, fill= BOTH, padx=5)
        ttk.Label(self, text="home").pack()


#create frame for global leaderboard
class GLFrame(ttk.Labelframe):
    def __init__(self, master):
        super().__init__(master.contentFrame, text="Global Leaderboard")
        self.pack(side = RIGHT, expand=True, fill= BOTH, padx=5)
        ttk.Label(self, text="global leaderboard").pack()

#create frame for private leaderboard
class PLFrame(ttk.Labelframe):
    def __init__(self, master):
        super().__init__(master.contentFrame, text="Global Leaderboard")
        self.pack(side = RIGHT, expand=True, fill= BOTH, padx=5)
        ttk.Label(self, text="test").pack()

#create frame for user stats
class userStats(ttk.Labelframe):
    def __init__(self, master):
        super().__init__(master.contentFrame, text="User Stats")
        self.pack(side = RIGHT, expand=True, fill= BOTH, padx=5)
        ttk.Label(self, text="search").pack()


#create frame for settings
class settings(ttk.Labelframe):


    def __init__(self, master):
        super().__init__(master.contentFrame, text="Settings")
        self.pack(side = RIGHT, expand=True, fill= BOTH, padx=5)

        theme = ttk.StringVar()
        darkmode = ttk.BooleanVar()

        #theme selector label
        ttk.Label(self, text= "Theme").grid(row=0, column=0, sticky="w", padx=5, pady=10)

        #theme selector
        ttk.OptionMenu(self, theme, "bootstrap", "pydata", "nord", "solarized", "catppuccin", "gruvbox", "dracula", "tokyo-night", "one", "everforest", "vapor", "minty", "pulse", "united", "sandstone").grid(row=0, column=1, sticky="e")

        #dark mode label
        ttk.Label(self, text= "Dark mode").grid(row=1, column=0, sticky="w", padx=5, pady=10)
        #dark mode checkbox
        ttk.Checkbutton(self, variable=darkmode, bootstyle="round toggle").grid(row=1, column=1, sticky="e", padx=5, pady=10)


        ttk.Button(self, text= "apply", command= lambda x = theme, y = darkmode: master.applySettings(x,y)).grid(column=1, sticky="s", padx=100, pady=25)

    

#loginGUI
#The login GUI should be put inside of the content window of the climbingApp class


global currentUser
currentUser = ""


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
    global createLabelFrame
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
    ttk.Button(createLabelFrame, text="Create account", bootstyle= PRIMARY, command=lambda: createButton(createUsername.get(), createPassword.get(), confirmPassword.get(), createLabelFrame)).pack(padx=10, pady=10, fill=X)



#function that is called when log in button is pressed
def loginButton(username, password, frame):
    global currentUser
    if login.login(username, password) == True:
        currentUser = username
        window.destroy()
    else:
        errorWidget("Wrong username or password", frame)
        return False




#function that is called when the create account button is pressed
def createButton(username, password, confirmPassword, frame):
    createErrorCheck(username, password, confirmPassword)
    if login.createAccount(username, password, confirmPassword) != False:
        accountCreated()
    


#widget to replace a frame with an error message
def errorWidget(error, frame):
    clearFrame(frame)
    photo = ttk.PhotoImage(file="resources/warning.png")
    label = ttk.Label(frame, image=photo)
    label.image = photo          
    label.pack(padx=20, pady=20)
    ttk.Label(frame, text=error).pack(padx=15, pady=30)
    ttk.Button(frame, text="Back", command=reset).pack()

#reset login menu to the first screen
def reset():
    firstMenu(window)

def createErrorCheck(username, password, confirmPassword):
    #check username not in use
    if login.checkUsername(username) == False:
        errorWidget("Username already exists", createLabelFrame)
    #check password meets requirements and passwords match
    elif login.checkPassword(password) != True:
        errorWidget("Password must have: \n-between 6 and 20 characters\n-at least one uppercase letter\n-at least one number\n-at least one special symbol", createLabelFrame)
    elif login.checkPasswordMatch(password, confirmPassword) != True:
        errorWidget("Passwords must match", createLabelFrame)

def accountCreated():
    clearFrame(createLabelFrame)
    photo = ttk.PhotoImage(file="resources/success.png")
    label = ttk.Label(createLabelFrame, image=photo)
    label.image = photo          
    label.pack(padx=20, pady=20)
    ttk.Label(createLabelFrame, text="Account created").pack(padx=15, pady=30)





app = climbingTracker()
climbingTracker.createSidebar(app)
app.mainloop()






#run app


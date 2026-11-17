import ttkbootstrap as ttk
import files as file
import login
import tracking
from ttkbootstrap.constants import *


pointsDictionary = {
	"V0": 1,
	"V1-2": 2,
	"V2-3": 5,
	"V2-4": 10,
	"V3-5": 25,
	"V4-6": 35,
	"V6-8": 50,
	"V8+": 75
	}

difficulties = ["V0", "V1-2", "V2-3", "V2-4", "V3-5", "V4-6", "V6-8", "V8+"]


#create window for GUI widgets
class climbingTracker(ttk.Window):
    def __init__(self):
        #give window properties (e.g. name, size and icon)
        super().__init__(title= "Climbing Tracker", size=(1280, 600), minsize=(600, 500), position=(400, 200), iconphoto="resources/logo.png")

        #create frame for content that will change
        self.contentFrame = ttk.Frame(self).pack(side=RIGHT, expand=True, fill=BOTH)


    def loadSettings(self):
        settings = file.load("settings")
        userTheme = "bootstrap"
        userMode = "light"
        for i in range(0, len(settings)):
            if settings[i][0] == currentUser:
                userTheme = settings[i][1]
                userMode = settings[i][2]
        self.theme_use(f"{userTheme}-{userMode}")



    def createSidebar(self):
        sidebar(self)

    def applySettings(self, theme, dark):
        settings = file.load("settings")
        mode = ""
        if dark.get() == False:
            mode = "light"
        elif dark.get() == True:
            mode = "dark"
        useTheme = theme.get()
        self.theme_use(f"{useTheme}-{mode}")
        foundUser = False
        for i in range(0, len(settings)):
            if currentUser == settings[i][0]:
                settings[i] = [currentUser, useTheme, mode]
                foundUser = True
        if foundUser == False:
            settings.append([currentUser, useTheme, mode])
        file.save(settings, "settings")


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

    #open the login menu in the main content frame
    def openLogin(self):
        self.clearFrame()
        loginFrame(self)

    def saveStats(self):
        accountStats = file.load("accountStats")
        for user in range(0, len(accountStats)):
            if accountStats[user][0] == currentUser:
                hardestClimb = tracking.calcHardest(currentUser)
                accountStats[user][1] = tracking.countPoints(currentUser)
                accountStats[user][2] = hardestClimb
                accountStats[user][3] = tracking.calcTotalAttempts(currentUser)
                accountStats[user][4] = tracking.countPoints(currentUser)
        file.save(accountStats, "accountStats")


#create sidebar
class sidebar(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(side=LEFT, fill="y", pady=5, padx=5)

        #add seperator for aesthetic purposes
        ttk.Separator(self, orient=VERTICAL, bootstyle=PRIMARY).pack(side=RIGHT, fill=Y, pady=10)

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
class home(ttk.Frame):
    def __init__(self, master):
        super().__init__(master.contentFrame)
        self.pack(side = RIGHT, expand=True, fill= BOTH, padx=5)

        userStatsFrame(self, self, currentUser).pack()

        #get stats
        accountStats = file.load("accountStats")
        for user in range(0, len(accountStats)):
            if accountStats[user][0] == currentUser:
                currentStats = accountStats[user]

        #entry widget variables
        attempts = ttk.IntVar()
        difficulty = ttk.StringVar()

        topFrame = ttk.Frame(self).pack(side=TOP, fill=X)

        ##log a climb
        logClimbFrame = ttk.Labelframe(topFrame, text="Log a climb").pack(fill= BOTH, padx=5, pady=5, side=LEFT, expand=True)
        ttk.Label(logClimbFrame, text="Difficulty").pack(padx=5, side=TOP)
        ttk.OptionMenu(logClimbFrame, difficulty, "V0", "V0", "V1-2", "V2-3", "V2-4", "V3-5", "V4-6", "V6-8", "V8+").pack(padx=5, pady=5, side=TOP)
        ttk.Label(logClimbFrame, text="Attempts").pack(padx=5, side=TOP)
        ttk.Entry(logClimbFrame, textvariable= attempts, bootstyle=PRIMARY).pack(padx=5, pady=5, side=TOP)


        def logClimb():
            attemptNumber = attempts.get()
            climbDifficulty = difficulty.get()
            tracking.addClimb(currentUser, climbDifficulty, attemptNumber)
            master.openHome()

        ttk.Button(logClimbFrame, text="Submit", bootstyle=PRIMARY, command= logClimb).pack(padx=5, pady=5)

        ##Points explainer
        pointsFrame = ttk.Labelframe(topFrame, text="Points").pack(fill= BOTH, padx=5, pady=5, side=RIGHT)
        ttk.Label(pointsFrame, text=f"{difficulties[0]}: {pointsDictionary[difficulties[0]]} point", anchor="w").grid(column=0, row=0, padx=5, sticky="w")
        for i in range(1, len(pointsDictionary)):
            ttk.Label(pointsFrame, text=f"{difficulties[i]}: {pointsDictionary[difficulties[i]]} points", anchor="w").grid(column=0, row=i, padx=5, sticky="w")

        bottomFrame = ttk.Frame(self).pack(side=BOTTOM, expand=True, fill=BOTH)

        ##goal
        #variables

        points = tracking.countPoints(currentUser)
        percentAcheived = (int(points) / int(currentStats[5])) * 100


        newGoal = ttk.IntVar()

        #change goal function
        def changeGoal():
            if newGoal.get() == "":
                return 1
            if newGoal.get() == 0:
                return 1
            else:
                tracking.changeGoal(currentUser, newGoal.get())
                master.openHome()

        #GUI
        goalFrame = ttk.Labelframe(bottomFrame, text="Target points").pack(expand=True, fill= BOTH, padx=5, pady=5, side=LEFT)
        meter = ttk.Meter(goalFrame, amount_used=percentAcheived, amount_format="{:.1f}", text_right="%", amount_min=0, subtext="of target", meter_type="semi", metersize=150).pack(padx=5, pady=5)
        lowerFrame = ttk.Frame(goalFrame).pack(side=BOTTOM, expand=True, fill=BOTH)
        changeFrame = ttk.Frame(lowerFrame).pack(side=LEFT, expand=True, fill = BOTH)
        ttk.Label(changeFrame, text="Change target").pack(padx=5, pady=5)
        ttk.Entry(changeFrame, textvariable=newGoal, bootstyle=PRIMARY).pack(padx=5, pady=5)
        ttk.Button(changeFrame, text= "Change", command=changeGoal, bootstyle=PRIMARY).pack(padx=5, pady=5)

        rightFrame = ttk.Frame(lowerFrame).pack(side=RIGHT, expand=True, fill=BOTH)
        ttk.Label(rightFrame, text=("Progress")).pack(pady=5)
        ttk.Label(rightFrame, text=f"{points}/{currentStats[5]}", bootstyle=PRIMARY, font="-size 36 -weight bold").pack(pady=12)

        ##User stats
        bottomRightFrame = ttk.Frame(bottomFrame).pack(side=RIGHT, expand=True, fill=BOTH)
        statsFrame = ttk.Labelframe(bottomRightFrame, text="Stats").pack(side=TOP, expand=True, fill=BOTH, padx=5, pady=5)
        ttk.Label(statsFrame, text=f"{points} points", bootstyle=PRIMARY, font="-size 18 -weight bold").pack()
        ttk.Label(statsFrame, text=f"Goal: {currentStats[5]}", anchor="w").pack()
        mostComClimb, totalClimbs = tracking.calcMostComClimb(currentUser)
        ttk.Label(statsFrame, text=f"Most common climb: {mostComClimb}, {totalClimbs} times").pack()
        ttk.Label(statsFrame, text=f"Hardest climb: {tracking.calcHardest(currentUser)}").pack()
        ttk.Label(statsFrame, text=f"Total attempts: {tracking.calcTotalAttempts(currentUser)}").pack()


        #position on leaderboard
        rankFrame = ttk.Labelframe(bottomRightFrame, text="Ranking").pack(expand=True, fill=BOTH, padx=5, pady=5, side=BOTTOM)
        numbOfUsers = len(accountStats)
        ttk.Label(rankFrame, text=f"#{findPosition(currentUser)}", bootstyle=PRIMARY, font="-size 36 -weight bold").pack(pady=12)
        ttk.Label(rankFrame, text=f"out of {numbOfUsers} users").pack()

        #save user stats
        master.saveStats()





#create frame for global leaderboard
class GLFrame(ttk.Labelframe):
    def __init__(self, master):
        super().__init__(master.contentFrame, text="Global Leaderboard")
        self.pack(side = RIGHT, expand=True, fill= BOTH, padx=5)

        def sortLeaderboard(array):
            for i in range(0, len(array)-1):
                    for j in range(0, len(array)-i-1):
                        if int(array[j][1]) < int(array[j+1][1]):
                            array[j], array[j+1] = array[j+1], array[j]
            return array

        accountStats = file.load("accountStats")
        tempArray = []
        for user in range(0, len(accountStats)):
            tempArray.append([accountStats[user][0], tracking.countPoints(accountStats[user][0])])


        leaderboard = ttk.Tableview(
            self,
            coldata=["Username", "Points"],
            rowdata=tempArray,
            bootstyle="primary",
            searchable=True,
            paginated=True,
            pagesize=10,
        )
        leaderboard.pack(fill="both", expand=True, padx=20, pady=20, side= TOP)
        leaderboard.sort_column_data(cid=1, sort=1)


class userStatsFrame(ttk.Labelframe):
    def __init__(self, master, frame, username):
        super().__init__(frame, text="Stats")


        accountStats = file.load("accountStats")
        for user in range(0, len(accountStats)):
            if accountStats[user][0] == username:
                currentStats = accountStats[user]

        points = tracking.countPoints(username)

        ttk.Label(self, text=f"{points} points", bootstyle=PRIMARY, font="-size 18 -weight bold").pack()
        ttk.Label(self, text=f"Goal: {currentStats[5]}", anchor="w").pack()
        mostComClimb, totalClimbs = tracking.calcMostComClimb(currentUser)
        ttk.Label(self, text=f"Most common climb: {mostComClimb}, {totalClimbs} times").pack()
        ttk.Label(self, text=f"Hardest climb: {tracking.calcHardest(currentUser)}").pack()
        ttk.Label(self, text=f"Total attempts: {tracking.calcTotalAttempts(currentUser)}").pack()










#create frame for private leaderboard
class PLFrame(ttk.Labelframe):
    def __init__(self, master):
        super().__init__(master.contentFrame, text="Private Leaderboard")
        self.pack(side = RIGHT, expand=True, fill= BOTH, padx=5)
        ttk.Label(self, text="test").pack()

#create frame for user stats
class userStats(ttk.Labelframe):
    def __init__(self, master):
        super().__init__(master.contentFrame, text="User Stats")
        self.pack(side = RIGHT, expand=True, fill= BOTH, padx=5)
        ttk.Label(self, text="search").pack()
        username = ttk.StringVar()
        ttk.Entry(self, textvariable= username, bootstyle=PRIMARY).pack()

        statsFrame = ttk.Frame(self).pack()

        def search():
            #clear frame
            for widget in statsFrame.winfo_children():
                widget.destroy()

            accountStats = file.load("accountStats")
            user = username.get()


            for i in range(0, len(accountStats)):
                if accountStats[i][0] == user:
                    statsArray = accountStats[i]

            ttk.Label(statsFrame, text=f"Username: {statsArray[0]}", bootstyle=PRIMARY).pack()
            ttk.Label(statsFrame, text=f"Total Points: {statsArray[1]}").pack()
            ttk.Label(statsFrame, text=f"Hardest Climb: {statsArray[2]}").pack()
            ttk.Label(statsFrame, text=f"Total Attempts: {statsArray[3]}").pack()


        ttk.Button(self, text="Search", bootstyle=PRIMARY, command=search).pack()



#create frame for settings
class settings(ttk.Labelframe):


    def __init__(self, master):
        super().__init__(master.contentFrame, text="Settings")
        self.pack(side = RIGHT, expand=True, fill= BOTH, padx=5)

        #column1 will stretch to fill the gap when the window is expanded
        self.columnconfigure(1, weight=1)

        #create necessary variables for input boxes
        theme = ttk.StringVar()
        darkmode = ttk.BooleanVar()

        #theme selector label
        ttk.Label(self, text= "Theme").grid(row=0, column=0, sticky="w", padx=5, pady=10)

        #theme selector
        ttk.OptionMenu(self, theme, "bootstrap", "bootstrap", "pydata", "nord", "solarized", "catppuccin", "gruvbox", "dracula", "tokyo-night", "one", "everforest", "vapor", "minty", "pulse", "united", "sandstone").grid(row=0, column=1, sticky="e", padx=5, pady=5)

        #dark mode label
        ttk.Label(self, text= "Dark mode").grid(row=1, column=0, sticky="w", padx=5, pady=10)
        #dark mode checkbox
        ttk.Checkbutton(self, variable=darkmode, bootstyle="round toggle").grid(row=1, column=1, sticky="e", padx=5, pady=10)


        ttk.Button(self, text= "Apply", command= lambda x = theme, y = darkmode: master.applySettings(x,y)).grid(column=1, sticky="s", padx=100, pady=25)



#Login GUI

#create class for frame with login system in
class loginFrame(ttk.Frame):
    global currentUser
    def __init__(self, master):
        #frame is placed within content frame in
        super().__init__(master.contentFrame)
        self.pack(expand=True, fill= BOTH, padx=5)

        #create variables for inputs
        loginUsername = ttk.StringVar()
        loginPassword = ttk.StringVar()

        createUsername = ttk.StringVar()
        createPassword = ttk.StringVar()
        confirmPassword = ttk.StringVar()

        #create frame for login system
        #this is necessary for a frame to display errors to appear
        content = ttk.Frame(self)
        content.pack(fill=BOTH, expand=True, padx=10, pady=20)

        # login section
        loginLabelFrame = ttk.Labelframe(content, text="Sign in")
        loginLabelFrame.pack(side=LEFT, fill=BOTH, expand=True, padx=10)

        #input for username
        ttk.Label(loginLabelFrame, text="Username").pack()
        ttk.Entry(loginLabelFrame, bootstyle=PRIMARY, textvariable= loginUsername).pack(padx=10, pady=10)

        #input for password
        ttk.Label(loginLabelFrame, text="Password").pack()
        ttk.Entry(loginLabelFrame, bootstyle= PRIMARY, textvariable=loginPassword, show="•").pack(padx=10, pady=10)


        #Button
        ttk.Button(loginLabelFrame, text="Log in", bootstyle= PRIMARY, command=lambda: self.loginButton(loginUsername.get(), loginPassword.get())).pack(padx=45, pady=20, fill=X)



        # separates both parts
        ttk.Separator(content, orient=VERTICAL, bootstyle=PRIMARY).pack(side=LEFT, fill=Y, pady=10)



        #create account section
        createLabelFrame = ttk.Labelframe(content, text="Create account")
        createLabelFrame.pack(side=LEFT, fill=BOTH, expand=True, padx=10)

        #input for username
        ttk.Label(createLabelFrame, text="Username").pack()
        ttk.Entry(createLabelFrame, bootstyle=PRIMARY, textvariable=createUsername).pack(padx=10, pady=10)

        #input for password
        ttk.Label(createLabelFrame, text="Password").pack()
        ttk.Entry(createLabelFrame, bootstyle= PRIMARY, textvariable=createPassword, show="•").pack(padx=10, pady=10)

        ttk.Label(createLabelFrame, text="Confirm Password").pack()
        ttk.Entry(createLabelFrame, bootstyle=PRIMARY, textvariable=confirmPassword, show="•").pack(padx=10, pady=10)

        #Button
        ttk.Button(createLabelFrame, text="Create account", bootstyle= PRIMARY, command=lambda: self.createButton(createUsername.get(), createPassword.get(), confirmPassword.get())).pack(padx=45, pady=20, fill=X)

    #method for when loginButton is pressed
    def loginButton(self, username, password):
        #check if login info is correct
        if login.login(username, password) == True:
            #initiallise main app
            #create global variable for current user that can be used to access the user's info when in main app
            global currentUser
            currentUser = username
            #load the settings for the main app
            climbingTracker.loadSettings(app)

            #create empty entry in accountStats

            #create UI components
            climbingTracker.createSidebar(app)
            climbingTracker.openHome(app)
        else:
            #show an error message
            self.errorWidget("Wrong username or password")

    #error message
    def errorWidget(self, error):
        errorWindow = ttk.Toplevel(master=self.master, title="Error!", position=(775, 475), size=(250, 300))
        photo = ttk.PhotoImage(file="resources/warning.png")
        #attach photo to label
        label = ttk.Label(errorWindow, image=photo)
        label.image = photo
        label.pack(padx=40, pady=20)
        #display error
        ttk.Label(errorWindow, text=error).pack(padx=15, pady=30)


    #reset screen to main login menu
    def reset(self):
        climbingTracker.openLogin(app)

    #method that gets called when "create account" button is pressed
    def createButton(self, username, password, confirmPassword):
        #check for errors
        self.createErrorCheck(username, password, confirmPassword)
        #attempt to create account
        if login.createAccount(username, password, confirmPassword) != False:
            #tell user that account is created
            self.accountCreated()
            tracking.initialliseAccountStats(username)
        return 0

    #check for errors when creating account
    def createErrorCheck(self, username, password, confirmPassword):
        #check username not in use
        if login.checkUsername(username) == False:
            self.errorWidget("Username already exists")
        #check password meets requirements and passwords match
        elif login.checkPassword(password) != True:
            self.errorWidget("Password must have: \n-between 6 and 20 characters\n-at least one uppercase letter\n-at least one number\n-at least one special symbol")
        elif login.checkPasswordMatch(password, confirmPassword) != True:
            self.errorWidget("Passwords must match")


    #show user that account has been created
    def accountCreated(self):
        successWindow = ttk.Toplevel(master=self.master, title="Success!", position=(775, 475), size=(250, 175))
        #load photo into memory
        photo = ttk.PhotoImage(file="resources/success.png")
        #attach photo to lable
        label = ttk.Label(successWindow, image=photo)
        label.image = photo
        label.pack(padx=20, pady=20)
        #display message
        ttk.Label(successWindow, text="Account created").pack(padx=15, pady=30)



def sortUsers():
    sortedUsers = file.load("accountStats")
    for i in range(len(sortedUsers)-1):
        for j in range(len(sortedUsers)-1-i):
            if int(sortedUsers[j][1]) < int(sortedUsers[j+1][1]):
                sortedUsers[j], sortedUsers[j+1] = sortedUsers[j+1], sortedUsers[j]
    return sortedUsers

def findPosition(username):
    array = sortUsers()
    for user in range(0, len(array)):
        if array[user][0] == username:
            return user + 1


print(sortUsers())



#run app
app = climbingTracker()
climbingTracker.openLogin(app)
app.mainloop()

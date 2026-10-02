import ttkbootstrap as ttk
import files as file
import login
from ttkbootstrap.constants import *

#create window for GUI widgets
class climbingTracker(ttk.Window):
    def __init__(self):
        #can also add icon if necessary
        super().__init__(title= "Climbing Tracker", size=(600, 500), iconphoto="resources/logo.png")

        #create sidebar and buttons on left
        pageFrame(self)

        #create frame for content that will change
        self.contentFrame = ttk.Frame(self).pack(side=RIGHT, expand=True, fill=BOTH)

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

    






#run app
app = climbingTracker()
app.mainloop()
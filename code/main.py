import ttkbootstrap as ttk
import files as file
import login
from ttkbootstrap.constants import *

#create window for GUI widgets
class climbingTracker(ttk.Window):
    def __init__(self):
        #can also add icon if necessary
        super().__init__(title= "Climbing Tracker", size=(600, 500))

        #create sidebar and buttons on left
        pageFrame(self)

        #create frame for content that will change
        self.contentFrame = ttk.Frame(self).pack(side=RIGHT, expand=True, fill=BOTH)

    #function to clear frame with changing content
    def clearFrame(self):
        for widget in self.contentFrame.winfo_children():
            widget.destroy()

    ###functions to display pages

    #display global leaderboard
    def openGlobalLeaderboard(self):
        self.clearFrame()
        GLFrame(self)


#create sidebar
class pageFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(side=LEFT, fill="y", pady=5, padx=5)

        #button for home menu
        ttk.Button(self, text="Home").pack(fill=BOTH, pady=5, padx=5)

        #button for global leaderboard
        ttk.Button(self, text="Global Leaderboard", command=master.openGlobalLeaderboard).pack(fill=BOTH, pady=5, padx=5)

        #button for private leaderboard
        ttk.Button(self, text="Private Leaderboard").pack(fill=BOTH, pady=5, padx=5)

        #add more buttons here:

#create frame for global leaderboard
class GLFrame(ttk.Labelframe):
    def __init__(self, master):
        super().__init__(master.contentFrame, text="Global Leaderboard")
        self.pack(side = RIGHT, expand=True, fill= BOTH, padx=5)
        ttk.Label(self, text="test").pack()


#run app
app = climbingTracker()
app.mainloop()
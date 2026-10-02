import ttkbootstrap as ttk
import files as file
import login
from ttkbootstrap.constants import *

#create window for GUI widgets
class climbingTracker(ttk.Window):
    def __init__(self):
        super().__init__(title= "Climbing Tracker", size=(500, 600))

        pageFrame(self)

        ttk.Labelframe(self, text="Home").pack(side=RIGHT, fill=BOTH, expand=True, padx=5)

#create frame for page options
class pageFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(side=LEFT, fill="y", pady=5, padx=5)
        ttk.Button(self, text="Home").pack(fill=BOTH, pady=5, padx=5)
        ttk.Button(self, text="Global Leaderboard").pack(fill=BOTH, pady=5, padx=5)
        ttk.Button(self, text="Private Leaderboard").pack(fill=BOTH, pady=5, padx=5)



class mainPage(ttk.Frame):
    def __init__(self, climbingTracker):
        super().__init__(climbingTracker, padding=16)
        self.pack()

        ttk.Label(self, text="Test").pack()

app = climbingTracker()
app.mainloop()
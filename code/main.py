import ttkbootstrap as ttk
import tkinter as tk
import files as file
import login

lightMode = True

def switchTheme():
    global lightMode
    if lightMode == True:
        app.theme_use("bootstrap-dark")
        lightMode = False
    else:
        app.theme_use("bootstrap-light")
        lightMode = True

app = ttk.App()
app.title = "Climbing tracker"

ttk.Button(app, text = "Change theme", command= switchTheme).pack(padx=25, pady=25)








app.mainloop()


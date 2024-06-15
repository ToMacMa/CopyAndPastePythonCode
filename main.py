import tkinter as tk
import clipboard

def onButtonClick(btnId):
    defaultBtnWindowSettings = list()
    defaultBtnWindowSettings.append("400x200")
    defaultBtnWindowSettings.append("400x400")

    if btnId == 1:
        btnWindow = tk.Tk()
        btnWindow.title("Tkinter copyables")
        btnWindow.geometry(defaultBtnWindowSettings[0])

        createBtnWindowContents(btnWindow,btnId)

        btnWindow.mainloop()
    if btnId == 2:
        btnWindow = tk.Tk()
        btnWindow.title("Math copyables")
        btnWindow.geometry(defaultBtnWindowSettings[0])
        
        createBtnWindowContents(btnWindow,btnId)

        btnWindow.mainloop()
    
    if btnId == 1-1:
        btnWindow = tk.Tk()
        btnWindow.title("Tkinter window with no contents")
        btnWindow.geometry(defaultBtnWindowSettings[1])

        createBtnWindowContents(btnWindow,btnId)

        btnWindow.mainloop()

    if btnId == 1-2:
        btnWindow = tk.Tk()
        btnWindow.title("Tkinter window with a button")
        btnWindow.geometry(defaultBtnWindowSettings[1])

        createBtnWindowContents(btnWindow,btnId)

        btnWindow.mainloop()

def createBtnWindowContents(btnWindow, btnId):
    if btnId == 1:
        button = tk.Button(btnWindow, text="Window with no contents",width=20,height=5, command= lambda: onButtonClick(1-1))
        button.place(x=0,y=0)

        button = tk.Button(btnWindow, text="Window with a button",width=20,height=5, command= lambda: onButtonClick(1-2))
        button.place(x=150,y=0)
    
    if btnId == 1-1:


        with open("./copyFiles/tkWindowNoContent.txt", "r") as file:
            contents = file.read()

        text = tk.Text(btnWindow,width=600,height=600); text.insert(1.0, contents); text.place(x=45,y=0)

        text.configure(state="disabled")
        text.configure(inactiveselectbackground=text.cget("selectbackground"))

        buttonRun = tk.Button(btnWindow, text="Run", width=5,height=5,command= lambda: runCode(contents))
        buttonRun.place(x=0,y=0)

        buttonCopy = tk.Button(btnWindow, text="Copy",width=5,height=5,command= lambda: copy2clip(contents))
        buttonCopy.place(x=0,y=90)
    if btnId == 1-2:


        with open("./copyFiles/tkWindowWithBtn.txt", "r") as file:
            contents = file.read()

        text = tk.Text(btnWindow,width=600,height=600); text.insert(1.0, contents); text.place(x=45,y=0)

        text.configure(state="disabled")
        text.configure(inactiveselectbackground=text.cget("selectbackground"))

        buttonRun = tk.Button(btnWindow, text="Run", width=5,height=5,command= lambda: runCode(contents))
        buttonRun.place(x=0,y=0)

        buttonCopy = tk.Button(btnWindow, text="Copy",width=5,height=5,command= lambda: copy2clip(contents))
        buttonCopy.place(x=0,y=90)

        

def runCode(code):
    exec(code)

def copy2clip(txt):
    clipboard.copy(txt)

def StartWindow(windowGeometry, title):
    root = tk.Tk()
    root.title(str(title))
    root.geometry(windowGeometry)

    button = tk.Button(root, text="Tkinter",width=10,height=5, command= lambda: onButtonClick(1))
    button.place(x=0,y=0)

    #button = tk.Button(root, text="Math",width=10,height=5, command= lambda: onButtonClick(2))
    #button.place(x=100,y=0)

    root.mainloop()

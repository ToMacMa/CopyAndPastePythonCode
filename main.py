import tkinter as tk

def StartWindow(windowGeometry):
    root = tk.Tk()
    root.geometry(windowGeometry)

    button1 = tk.Button(root, text="Tkinter")
    button1.place(x=0,y=0)

    root.mainloop()

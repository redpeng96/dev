import time
import tkinter.ttk as ttk
from tkinter import *


root = Tk()
root.title("TITLE")
root.geometry("800x600+300+100")


def btncmd():
    pass


btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()
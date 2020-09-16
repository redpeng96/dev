import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("PROGRESS BAR")
root.geometry("800x600+300+100")

progressbar = ttk.Progressbar(root, maximum=100, length=150, mode="indeterminate")
progressbar.start(5)
progressbar.pack()

Label(root).pack()

progressbar2 = ttk.Progressbar(root, maximum=100, length=200, mode="determinate")
progressbar2.start(10)
progressbar2.pack()

def btncmd():
    progressbar2.stop()

btn = Button(root, text="STOP", command=btncmd)
btn.pack()

Label(root).pack()

p_var3 = DoubleVar()
progressbar3 = ttk.Progressbar(root, maximum=100, length=250, variable=p_var3)
progressbar3.pack()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.05)
        p_var3.set(i)
        progressbar3.update()
        print(p_var3.get())

btn2 = Button(root, text="START", command=btncmd2)
btn2.pack()

root.mainloop()
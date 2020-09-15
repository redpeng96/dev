import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("COMBO BOX")
root.geometry("800x600+300+100")

values = [str(i) + "일" for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.set("Select date...")
combobox.pack()

def btncmd():
    print(combobox.get())


btn = Button(root, text="SELECT", command=btncmd)
btn.pack()

root.mainloop()
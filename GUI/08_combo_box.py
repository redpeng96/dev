import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("COMBO BOX")
root.geometry("800x600+300+100")

Label(root, text="Select Month").pack()
values1 = [str(i) + "월" for i in range(1, 13)]
ro_combobox = ttk.Combobox(root, height=12, values=values1, state="readonly")
ro_combobox.current(0)
ro_combobox.pack()

Label(root, text="Select Day").pack()
values2 = [str(i) + "일" for i in range(1, 32)]
combobox = ttk.Combobox(root, height=15, values=values2)
combobox.set("Select date...")
combobox.pack()

def btncmd():
    print(ro_combobox.get(), combobox.get())

btn = Button(root, text="SELECT", command=btncmd)
btn.pack()

root.mainloop()
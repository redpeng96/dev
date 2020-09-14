from tkinter import *

root = Tk()
root.title("Daily Update")
root.geometry("800x600+300+100")

txt = Text(root, width=50, height=5)
txt.pack()
txt.insert(END, "Input: ")

e = Entry(root, width=40)
e.pack()
e.insert(0, "Input one line: ")


def btncmd():
    pass

btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()
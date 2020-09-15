from tkinter import *

root = Tk()
root.title("CHECK BOX")
root.geometry("800x600+300+100")

chkvar = IntVar()
chkbox = Checkbutton(root, text="Do not see for a day!", variable=chkvar)
#chkbox.select()
#chkbox.deselect()
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="Do not see for a week!", variable=chkvar2)
chkbox2.pack()


def btncmd():
    print(chkvar.get())
    print(chkvar2.get())


btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()
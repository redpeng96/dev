import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("MESSAGE BOX")
root.geometry("800x600+300+100")

def info():
    msgbox.showinfo("INFO", "This is an INFO message!")

def warn():
    msgbox.showwarning("WARNING", "This is an WARNING message!")

def error():
    msgbox.showerror("ERROR", "This is an ERROR message!")

def okcancel():
    msgbox.askokcancel("OK? CANCEL?", "Will you proceed further?")

def retrycancel():
    msgbox.askretrycancel("RETRY? CANCEL?", "Will you try again?")

def yesno():
    msgbox.askyesno("YES? NO?", "Continue?")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="Continue?\nCancel?")
    print("SELECTION: ", response)
    if response == 1:
        print("YES")
    elif response == 0:
        print("NO")
    else:
        print("CANCEL")


Button(root, command=info, text="ALERT").pack()
Button(root, command=warn, text="WARNING").pack()
Button(root, command=error, text="ERROR").pack()
Button(root, command=okcancel, text="OK/CANCEL").pack()
Button(root, command=retrycancel, text="RETRY/CANCEL").pack()
Button(root, command=yesno, text="YES/NO").pack()
Button(root, command=yesnocancel, text="YES/NO/CANCEL").pack()


root.mainloop()
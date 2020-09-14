from tkinter import *

root = Tk()
root.title("Daily Update")
root.geometry("800x600+300+100")

label1 = Label(root, pady=30, text="Hello World!")
label1.pack()

photo = PhotoImage(file="./GUI/btn6.png")
label2 = Button(root, image=photo)
label2.pack()

def chgchar():
    label1.config(text="Good Bye")
    global photo2
    photo2 = PhotoImage(file="./GUI/btn66.png")
    label2.config(image=photo2)

btn = Button(root, text="Click to Change the label", command=chgchar)
btn.pack()



root.mainloop()
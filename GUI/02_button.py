from tkinter import *

root = Tk()
root.title("Daily Update")
root.geometry("800x600+300+100")

btn1 = Button(root, text="BUTTON-01")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="BUTTON-02")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="BUTTON-03")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="BUTTON-04")
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="BUTTON-05")
btn5.pack()

photo = PhotoImage(file="./GUI/btn6.png")
btn6 = Button(root, image=photo)
btn6.pack()


def btncmd():
    print("Button7 clicked!!!")
btn7 = Button(root, text="BUTTON-07", command=btncmd)
btn7.pack()


root.mainloop()
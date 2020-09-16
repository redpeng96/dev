from tkinter import *

root = Tk()
root.title("FRAME")
root.geometry("800x600+300+100")


def btncmd():
    pass

Label(root, text="SELECT MENU").pack(side="top")
Button(root, text="ORDER").pack(side="bottom")


frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)
Button(frame_burger, text="Hamburger").pack()
Button(frame_burger, text="Cheese Burger").pack()
Button(frame_burger, text="Bacon Burger").pack()


frame_drink = LabelFrame(root, text="DRINKS", relief="solid", bd=1)
frame_drink.pack(side="right", fill="both", expand=True)
Button(frame_drink, text="Coke").pack()
Button(frame_drink, text="Sprite").pack()


root.mainloop()
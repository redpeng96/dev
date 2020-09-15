from tkinter import *

root = Tk()
root.title("RADIO BUTTON")
root.geometry("800x600+300+100")

Label(root, text="Select your menu!").pack()

burger_var = IntVar()
btn_burger1 = Radiobutton(root, text="Hamburger", value=1, variable=burger_var)
btn_burger2 = Radiobutton(root, text="Cheese Burger", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="Bacon Burger", value=3, variable=burger_var)
btn_burger1.select()
btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root).pack()
Label(root, text="Select your drink!").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="Coca Cola", value="CK", variable=drink_var)
btn_drink2 = Radiobutton(root, text="Sprite", value="SPT", variable=drink_var)
btn_drink3 = Radiobutton(root, text="Root Beer", value="RB", variable=drink_var)
btn_drink1.select()
btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()


def btncmd():
    print(burger_var.get())
    print(drink_var.get())


btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()
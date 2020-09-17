from tkinter import *

root = Tk()
root.title("GRID")
root.geometry("800x600+300+100")

#btn1 = Button(root, text="1", padx=10, pady=10)
#btn2 = Button(root, text="2", padx=10, pady=10)
#btn3 = Button(root, text="3", padx=10, pady=10)
#btn4 = Button(root, text="ENTER", padx=10, pady=10)
#btn5 = Button(root, text="0", padx=10, pady=10)
#btn6 = Button(root, text=".", padx=10, pady=10)

btn1 = Button(root, text="1", width=5, height=3)
btn2 = Button(root, text="2", width=5, height=3)
btn3 = Button(root, text="3", width=5, height=3)
btn4 = Button(root, text="ENTER\nOR\nWHAT", width=5, height=3)
btn5 = Button(root, text="0", width=5, height=3)
btn6 = Button(root, text=".", width=5, height=3)

#btn1.pack(side="left")


btn1.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn2.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn3.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn4.grid(row=0, column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3)
btn5.grid(row=1, column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3)
btn6.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)

root.mainloop()



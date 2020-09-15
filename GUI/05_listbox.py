from tkinter import *

root = Tk()
root.title("LIST BOX")
root.geometry("800x600+300+100")

listbox = Listbox(root, selectmode="extended", height=0)
#listbox = Listbox(root, selectmode="single", height=2)

listbox.insert(0, "APPLE")
listbox.insert(1, "STRAWBERRY")
listbox.insert(2, "BANANA")
listbox.insert(END, "WATERMELON")
listbox.insert(END, "GRAPE")
listbox.pack()


def btncmd():
    #listbox.delete(END)
    #listbox.delete(0)
    print(listbox.size())
    print(listbox.get(0, 2))
    
    ### Return the indexes of current selection.
    print(listbox.curselection())


btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()
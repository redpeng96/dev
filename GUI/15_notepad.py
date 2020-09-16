import os
from tkinter import *

root = Tk()
root.title("Windows Notepad")
root.geometry("800x600+300+100")

filename = "mynote.txt"

def open_file():
    if os.path.isfile(filename):
        f = open(filename, "r")
        txt.delete("1.0", END)
        txt.insert(END, f.read())

def save_file():
    f = open(filename, "w")
    f.write(txt.get("1.0", END))
    f.close()

menu = Menu(root)

# File menu
#=====================================================================
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="Open", command=open_file)
menu_file.add_command(label="Save", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="Quit", command=root.quit)

menu.add_cascade(label="File(F)", menu=menu_file)


# Edit menu
#=====================================================================
menu_edit = Menu(menu, tearoff=0)
menu.add_cascade(label="Edit(E)", menu=menu_edit)


# Format menu
#=====================================================================
menu_format = Menu(menu, tearoff=0)
menu.add_cascade(label="Format(O)", menu=menu_format)


# View menu
#=====================================================================
menu_view = Menu(menu, tearoff=0)
menu.add_cascade(label="View(V)", menu=menu_view)


# Help menu
#=====================================================================
menu_help = Menu(menu, tearoff=0)
menu.add_cascade(label="Help(H)", menu=menu_help)



scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", expand=True, fill="both")

scrollbar.config(command=txt.yview)



root.config(menu=menu)
root.mainloop()
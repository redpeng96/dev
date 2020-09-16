
from tkinter import *

root = Tk()
root.title("MENU")
root.geometry("800x600+300+100")

def create_new_file():
    print("01. New File Created..........")

def create_new_window():
    print("02. New Window Created..........")

def open_new_file():
    print("03. New File Opened..........")

menu = Menu(root)

#=====================================================================
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window", command=create_new_window)
menu_file.add_separator()
menu_file.add_command(label="Open", command=open_new_file)
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable")
menu_file.add_separator()
menu_file.add_command(label="Quit", command=root.quit)

menu.add_cascade(label="File", menu=menu_file)
#=====================================================================

menu_file2 = Menu(menu)
menu.add_cascade(label="Edit", menu=menu_file2)


menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=menu_lang)


menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show minimap")
menu.add_cascade(label="View", menu=menu_view)


root.config(menu=menu)
root.mainloop()
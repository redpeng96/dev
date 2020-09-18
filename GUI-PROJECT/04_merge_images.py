import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog
from PIL import Image
import os


root = Tk()
root.title("Image Merger")
root.resizable(False, False)

### File Frame
def add_file():
    files = filedialog.askopenfilenames(title="Select image files...", filetypes=(("PNG files", "*.png"), ("ALL Files", "*.*")), initialdir="C:/")
    for file in files:
        list_box.insert(END, file)

def del_file():
    for idx in reversed(list_box.curselection()):
        list_box.delete(idx)


file_frame = Frame(root)
file_frame.pack(fill="x")

btn_add_file = Button(file_frame, padx=10, pady=10, width=15, text="Add File", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=10, pady=10, width=15, text="Delete File", command=del_file)
btn_del_file.pack(side="right")


### List Frame

list_frame = Frame(root)
list_frame.pack(fill="both", padx=10, pady=10)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_box = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_box.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_box.yview)


### Save Path Frame

def browse_dst_path():
    dst_dir = filedialog.askdirectory()
    if dst_dir == '':
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, dst_dir)


path_frame = LabelFrame(root, text="SAVE PATH")
path_frame.pack(fill="x", padx=10, pady=10)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand="y", ipady=4)

btn_dest_path = Button(path_frame, text="FIND", width=10, command=browse_dst_path)
btn_dest_path.pack(side="right")


### Option Frame

option_frame = LabelFrame(root, text="OPTIONS")
option_frame.pack(padx=10, pady=10)

## 1. Width Option
lbl_width = Label(option_frame, text="WIDTH", width=8)
lbl_width.pack(side="left")

opt_width = ["Keep", "1024", "800", "640"]
cmb_width = ttk.Combobox(option_frame, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

## 2. Space Option
lbl_space = Label(option_frame, text="SPACE", width=8)
lbl_space.pack(side="left")

opt_space = ["None", "Narrow", "Normal", "Large"]
cmb_space = ttk.Combobox(option_frame, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

## 3. Format Option
lbl_format = Label(option_frame, text="format", width=8)
lbl_format.pack(side="left", padx=10, pady=10)

opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(option_frame, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="right", padx=5, pady=5)


### Progress Bar

frame_progress = LabelFrame(root, text="Progress")
frame_progress.pack(fill="x", padx=10, pady=10)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=10, pady=10)



### Run Frame
def merge_image():
    images = [Image.open(x) for x in list_box.get(0, END)]
    widths = [x.size[0] for x in images]
    heights = [x.size[1] for x in images]

    # Get background size
    max_width, total_height = max(widths), sum(heights)
    # Create background
    result_img = Image.new("RGB", (max_width, total_height), (255, 255, 255))
    y_offset = 0
    for idx, img in enumerate(images):
        result_img.paste(img, (0, y_offset))
        y_offset += img.size[1]

        progress = (idx +1) / len(images) * 100
        p_var.set(progress)
        progress_bar.update()

    dest_path = os.path.join(txt_dest_path.get(), "result.jpg")
    result_img.save(dest_path)
    msgbox.showinfo("Info", "The job has been finished...")


def start():
    if list_box.size() == 0:
        msgbox.showwarning("Warning", "Add image files...")
        return
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("Warning", "Input save path...")
        return
    merge_image()

frame_run = Frame(root)
frame_run.pack(fill="x", padx=10, pady=10)

btn_start = Button(frame_run, padx=5, pady=5, text="START", width=12, command=start)
btn_start.pack(side="right")

btn_close = Button(frame_run, padx=5, pady=5, text="CLOSE", width=12, command=root.quit)
btn_close.pack(side="left")



root.mainloop()


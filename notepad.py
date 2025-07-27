from tkinter import*

root = Tk()
root.title("Notepad")
root.geometry("400x300")

def new_file():
    print("New File opened")

def open_file():
    print("File Opened")

def cut_text():
    print("Cut")

def copy_text():
    print("Copy")

def paste_text():
    print("Paste")

def undo_action():
    print("Undo")                   

menubar = Menu(root)

file = Menu(menubar,tearoff=0)
file.add_command(label="New",command=new_file)
file.add_command(label="New File")
file.add_command(label="Open File",command=open_file)
file.add_command(label="Current",command=cut_text)
file.add_command(label="Save",command=copy_text)
file.add_command(label="Save as",command=paste_text)
file.add_command(label="New Window",command=undo_action)
file.add_separator()
file.add_command(label="Exit",command=root.quit)
menubar.add_cascade(label="File",menu=file)

edit = Menu(menubar,tearoff=0)
edit.add_command(label="Cut",command=cut_text)
edit.add_command(label="Copy",command=copy_text)
edit.add_command(label="Paste",command=paste_text)
edit.add_command(label="Undo",command=undo_action)
edit.add_separator()
menubar.add_cascade(label="Edit",menu=edit)

view = Menu(menubar,tearoff=0)
view.add_command(label="Zoom out")
view.add_command(label="Zoom in")
view.add_separator()
menubar.add_cascade(label="View",menu=view)


root.config(menu=menubar)

root.mainloop()

import tkinter as TK
from tkinter import filedialog, messagebox

def new_file():
    text.delete(1.0, TK.END)

def open_file():
        file_path = filedialog.askopenfilename(defaultextension = "txt", filetypes = [("Text Files",".txt")])
        if file_path:
            with open(file_path, 'r')as file:   
                text.delete(1.0, TK.END)
                text.insert(TK.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=["Text File",".txt"])
    if file_path:
        with open(file_path,'w')as file:
            file.write(text.get(1.0, TK.END))
            messagebox.showinfo("Info", "File Saves Successfully!")

root = TK.Tk()
root.title("Simple Text Editor")
root.geometry("800x600")

menu = TK.Menu(root)
root.config(menu=menu)

file_menu = TK.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator
file_menu.add_command(label="Exit", command=root.quit)

text = TK.Text(root, wrap=TK.WORD, font=("Helvetica", 12), fg="blue")
text.pack(expand=TK.YES, fill=TK.BOTH)

root.mainloop()

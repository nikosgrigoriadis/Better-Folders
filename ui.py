import tkinter as tk
from tkinter import filedialog
from tkinter import Label
from main import backend
from main import Set_pathS
from main import Set_pathD
from main import Checkbox_value
from main import Set_input


def choose_fileS():
    filepath = filedialog.askdirectory()
    sourcelabel = Label(root, text=filepath)  # emfanisi path
    sourcelabel.pack()
    Set_pathS(filepath)


def choose_fileD():
    filepath = filedialog.askdirectory()
    sourcelabel = Label(root, text=filepath)  # emfanisi path
    sourcelabel.pack()
    Set_pathD(filepath)


def checkbox_statement(): # DIORTHOSI KOUMPIOU NA PAIRNEI TO VALUE ME 1 CLICK
    user_input = text_input.get()
    text_input.pack()
    if checkbox_state.get():

        Set_input(user_input)
        Checkbox_value(True)
    else:
        text_input.pack_forget()
        Checkbox_value(False)


root = tk.Tk()
root.geometry("400x200")
checkbox_state = tk.BooleanVar()
checkbox_state.set(False)
text_input = tk.Entry(root)

source_folder = tk.Button(root, text="Source Folder", command=choose_fileS)
destination_folder = tk.Button(root, text="Destination Folder", command=choose_fileD)
execute = tk.Button(root, text="Execute!", command=backend)
checkbox = tk.Checkbutton(root, text="Create Folder", variable=checkbox_state, command=checkbox_statement)

source_folder.pack()
destination_folder.pack()
execute.pack()
checkbox.pack()

root.mainloop()

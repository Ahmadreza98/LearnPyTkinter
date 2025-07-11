# import tkinter library
import tkinter as tk
from tkinter import ttk

# create a build_app function
def build_app():
    # create a root window
    window = tk.Tk()
    # set the title of the window
    window.title("Tkinter App (Tabs Example)")
    # set the size of the window
    window.geometry("400x300")
    
    # create a notebook
    note = ttk.Notebook(window, width=250, height=250,)
    # create several tabs
    tab1 = ttk.Frame(note)
    tab2 = ttk.Frame(note)
    note.add(tab1, text="Tab 1")
    note.add(tab2, text="Tab 2")
    # create a button in tab1
    button1 = ttk.Button(tab1, text="Button in Tab 1")
    button1.pack(pady=20)
    # create a label in tab2
    label2 = ttk.Label(tab2, text="Label in Tab 2")
    label2.pack(pady=20)
    
    note.pack()
    # run app
    window.mainloop()

if __name__ == "__main__":
    # call the build_app function
    build_app()
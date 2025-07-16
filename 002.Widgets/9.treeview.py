# import tkinter library
import tkinter as tk
from tkinter import ttk

# build app
def build_app():
    # create a window
    window = tk.Tk()
    # set window title
    window.title("Tkinter App with TreeView")
    # create a TreeView widget
    tree = ttk.Treeview(window, columns=("Name", "Age"))
    tree.heading("#0", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Age", text="Age")
    tree.insert("", "end", text="1", values=("Alice", 30))
    tree.insert("", "end", text="2", values=("Alice", 30))
    tree.insert("", "end", text="3", values=("Alice", 30))
    tree.insert("", "end", text="4", values=("Alice", 30))
    tree.pack()
    # set window size
    window.geometry("700x300")
    # run app
    window.mainloop()

if __name__ == "__main__":
    build_app()
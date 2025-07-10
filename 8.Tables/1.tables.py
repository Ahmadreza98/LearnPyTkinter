#import Tkinter library
import tkinter as tk
from tkinter import ttk

# Create biuld app function
def biuld_app():
    # Create the main window
    window = tk.Tk()
    # Set window title
    window.title("Tkinter App (TreeView)")
    # Set window size
    window.geometry("450x300")
    # import data
    names = ["Alice", "Bob", "Charlie", "David"]
    family = ["Smith", "Johnson", "Williams", "Jones"]
    # treeview
    table = ttk.Treeview(window, columns=("Names", "Family"), show="headings")
    table.heading("Names", text="Names")
    table.heading("Family", text="Family")
    
    for ind,val in enumerate(names):
        table.insert("", "end", values=(val, family[ind]))
    
    table.pack(fill="both", expand=True)
    
    # run app
    window.mainloop()

if __name__ == "__main__":
    biuld_app()
# import tkinter library
import tkinter as tk
from tkinter import ttk

# build_app function
def build_app():
    # create main root
    window = tk.Tk()
    # set title
    window.title("Tkinter App (window features)")
    # set size
    window.geometry("400x300")
    
    # set min and max size
    window.minsize(400,300)
    window.maxsize(800,600)
    
    # set fix size window
    window.resizable(False,False)
    
    # set icon for window
    icon = tk.PhotoImage(file="./ico.png")
    window.iconphoto(False,icon)
    
    # run app
    window.mainloop()

if __name__ == "__main__":
    build_app()
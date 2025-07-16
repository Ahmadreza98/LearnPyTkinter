# import tkinter library
import tkinter as tk
from tkinter import ttk


# build_app function
def build_app():
    # create main root
    window = tk.Tk()
    # set window of title
    window.title("Tkinter App (Menu Example)")
    # set window of size
    window.geometry("400x300")
    
    # create a menubar
    menubar = tk.Menu(window)
    
    # create sub-menubar
    sub_menubar = tk.Menu(menubar, tearoff=False)
    sub_menubar.add_command(label="New", command= lambda: print("Hello New!"))
    sub_menubar.add_command(label="Open", command= lambda: print("Hello Open!"))
    sub_menubar.add_separator()
    sub_menubar.add_command(label="Exit", command=window.quit)
    
    # add menubar in window
    menubar.add_cascade(label="File", menu=sub_menubar)
    
    # root config
    window.config(menu=menubar)
    
    # run app
    window.mainloop()

if __name__ == "__main__":
    build_app()
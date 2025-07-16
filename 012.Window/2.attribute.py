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
    
    # set transparent
    window.attributes("-alpha", 0.8)
    
    # set fullscreen
    # window.attributes("-fullscreen",True) 
    
    # set topmost
    window.attributes("-topmost",True)
    
    # run app
    window.mainloop()

if __name__ == "__main__":
    build_app()
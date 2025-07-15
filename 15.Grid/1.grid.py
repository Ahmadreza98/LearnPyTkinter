# import tkinter library
import tkinter as tk
from tkinter import ttk

# build_app function
def build_app():
    # main application window
    window = tk.Tk()
    window.title("Tkinter App (Grid Layout)")
    window.geometry("500x300")
    window.configure(padx=10, pady=10)
    
    
    
    window.mainloop()

if __name__ == "__main__":
    build_app()
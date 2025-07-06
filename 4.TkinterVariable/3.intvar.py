#import tkinter library
import tkinter as tk
from tkinter import ttk

# build app
def build_app():
    # create a window
    window = tk.Tk()
    # set window title
    window.title("Tkinter App")
    # set window size
    window.geometry("400x300")
    # define integer variable
    int_var = tk.IntVar()
    # define widgets
    lbl = ttk.Label(window, text="Hello, Tkinter!")
    lbl.pack(pady=20)
    
    eny = ttk.Entry(window, width=30, textvariable=int_var)
    eny.pack(pady=20)
    
    btn = ttk.Button(window, text="Click Me", command=lambda: lbl.config(text=f"Value: {int_var.get()}"))
    btn.pack(pady=20)
    
    # run app
    window.mainloop()

if __name__ == "__main__":
    build_app()
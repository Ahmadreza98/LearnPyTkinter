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
    # define boolean variable
    bool_var = tk.BooleanVar()
    # define widgets
    lbl = ttk.Label(window, text="Hello, Tkinter!")
    lbl.pack(pady=20)
    
    eny = ttk.Entry(window, width=30)
    eny.pack(pady=20)
    
    btn = ttk.Button(window, text="Click Me")
    btn.pack(pady=20)
    
    cbtn1 = ttk.Checkbutton(window, text="Option 1")
    cbtn1.pack(pady=5)
    rbtn1 = ttk.Radiobutton(window, text="Option 1", variable=bool_var, value=True, command=lambda: lbl.config(text=f"Option 1 selected: {bool_var.get()}"))
    rbtn1.pack(pady=5)
    rbtn2 = ttk.Radiobutton(window, text="Option 2", variable=bool_var, value=False, command=lambda: lbl.config(text=f"Option 2 selected: {bool_var.get()}"))
    rbtn2.pack(pady=5)
    
    
    # run app
    window.mainloop()

if __name__ == "__main__":
    build_app()
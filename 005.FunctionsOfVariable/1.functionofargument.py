#import tkinter library
import tkinter as tk
from tkinter import ttk

# Button function
def btn_func(str_var):
    # define a function to be called when button is clicked
    def on_click():
        # print the value of the variable
        print(str_var.get())
    return on_click

# build app
def build_app():
    # create a window
    window = tk.Tk()
    # set window title
    window.title("Tkinter App")
    # set window size
    window.geometry("400x300")
    # create a value variable
    str_var = tk.StringVar(value="Hello, Tkinter!")
    # define a entry widget
    entry = ttk.Entry(window, width=30, textvariable=str_var)
    entry.pack(pady=20)
    # define a button widget
    btn = ttk.Button(window, text="Click Me", command=btn_func(str_var))
    btn.pack(pady=10)
    # run app
    window.mainloop()

if __name__ == "__main__":
    build_app()
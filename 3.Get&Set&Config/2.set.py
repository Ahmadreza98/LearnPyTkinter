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
    # define widgets
    var = tk.StringVar()
    entry = ttk.Entry(window, textvariable=var)
    entry.pack(pady=20)
    var.set("John Doe")  # Sets the entry value
    # run app
    window.mainloop()

if __name__ == "__main__":
    build_app()
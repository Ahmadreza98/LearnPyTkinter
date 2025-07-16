# import tkinter library
import tkinter as tk
from tkinter import ttk

# build app
def build_app():
    # create a window
    window = tk.Tk()
    # set window title
    window.title("Tkinter App with Progressbar")
    # create a Progressbar widget
    progbar = ttk.Progressbar(window, length=200, mode="determinate")
    progbar['value'] = "50"
    progbar.pack() 
    # set window size
    window.geometry("400x300")
    # run app
    window.mainloop()

if __name__ == "__main__":
    build_app()
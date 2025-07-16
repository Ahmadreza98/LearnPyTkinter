# import tkinter library
import tkinter as tk
from tkinter import ttk

# build app
def build_app():
    # create a window
    window = tk.Tk()
    # set window title
    window.title("Tkinter App with scale")
    # create a scale widget
    scale = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL)
    scale.pack()
    # set window size
    window.geometry("400x300")
    # run app
    window.mainloop()

if __name__ == "__main__":
    build_app()
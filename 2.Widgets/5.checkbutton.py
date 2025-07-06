# import tkinter library
import tkinter as tk
from tkinter import ttk

# build app
def build_app():
    # create a window
    window = tk.Tk()
    # set window title
    window.title("Tkinter App with check button")
    # create a check button widget
    frm = ttk.Checkbutton(window, text="Check me!")
    frm.pack() 
    # set window size
    window.geometry("400x300")
    # run app
    window.mainloop()

if __name__ == "__main__":
    build_app()
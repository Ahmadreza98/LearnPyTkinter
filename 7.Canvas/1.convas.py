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
    # create canvas
    canvas = tk.Canvas(window, width=300, height=200, bg="white")
    canvas.pack()
    # draw a rectangle
    canvas.create_rectangle(50,50,150,150,fill="gray", width=5, dash=(5,100)) 
    # run app
    window.mainloop()

if __name__ == "__main__":
    build_app()
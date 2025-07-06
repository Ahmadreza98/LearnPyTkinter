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
    eny = ttk.Entry(window, width=30)
    eny.pack(pady=20)
    
    btn = ttk.Button(window, text="Click Me", command=lambda: print(f"Hello, {eny.get()}!"))
    btn.pack(pady=20)
    
    # run app
    window.mainloop()

if __name__ == "__main__":
    build_app()
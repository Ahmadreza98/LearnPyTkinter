# import tkinter library
import tkinter as tk
from tkinter import ttk

# build_app function
def build_app():
    # create main root
    window = tk.Tk()
    # set title
    window.title("Tkinter App (Pack Example)")
    # set size
    window.geometry("450x300")
    # set padying main window
    window.config(padx=10, pady=10)
    
    # create Labels area
    lbl1 = ttk.Label(window, text="Area 1", background="#ccf458").pack(side="top", fill="both")
    lbl4 = ttk.Label(window, text="Area 1", background="#f4586a").pack(side="bottom", fill="both")
    lbl2 = ttk.Label(window, text="Area 1", background="#f48458").pack(side="left", fill="both")
    lbl3 = ttk.Label(window, text="Area 1", background="#58f4ec").pack(side="right", fill="both")
    
    # run app
    window.mainloop()    
    

if __name__ == "__main__":
    build_app()
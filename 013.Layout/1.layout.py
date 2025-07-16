# import tkinter library
import tkinter as tk
from tkinter import ttk

# build_app function
def build_app():
    # create a main root
    window = tk.Tk()
    # set title window
    window.title("Tkinter App (Layout Example)")
    # set window size
    window.geometry("400x300")
    
    # create labels in main window
    lbl1 = ttk.Label(window, text="this is Label 1.", background="#458ccc")
    lbl2 = ttk.Label(window, text="this is Label 2.", background="#32cff1")
    
    # set Labels with pack()
    ## lbl1.pack(side="left", expand=True,  fill="x")
    ## lbl2.pack(side="right", expand=True, fill="x")
    
    # set config for use grid()
    ## for i in range(4):
    ##    window.grid_rowconfigure(i,weight=1)
    ##    window.grid_columnconfigure(i, weight=1)
    # set Labels with grid()
    ## lbl1.grid(row=1, column=1)
    ## lbl2.grid(row=3, column=2) 
    
    # set Labels with place()
    lbl1.place(x=0,y=200)
    lbl2.place(x=0,y=250)
    
    # run app
    window.mainloop()

if __name__ == "__main__":
    build_app()
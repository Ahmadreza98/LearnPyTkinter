# import tkinter library
import __main__
import tkinter as tk
from tkinter import ttk

# create build_app function
def build_app():
    # create main root
    window = tk.Tk()
    # set a title root
    window.title("Tkinter App (Frame Example)")
    # set a size root
    window.geometry("450x300")
    
    # create a frame in root
    frame = ttk.Frame(window, padding="15",width=300, height=250, borderwidth=10, relief="groove")
    frame.pack()
    # prevent auto-size frame
    frame.pack_propagate(False)
    # create buttons in frame
    btn = ttk.Button(frame, text="Click Me!", command=lambda: print("Click clicked!"))
    btn.pack(pady=10)
    btn = ttk.Button(frame, text="Submit!", command=lambda: print("Submit clicked!"))
    btn.pack(pady=10)
    #crate labels in frame
    lbl = ttk.Label(frame, text="This is a label-1 in a frame.")
    lbl.pack(pady=10)
    lbl = ttk.Label(frame, text="This is a label-2 in a frame.")
    lbl.pack(pady=10)

    
    # run app
    window.mainloop()
    
# check if this file is run directly
if __name__ == "__main__":
    build_app()
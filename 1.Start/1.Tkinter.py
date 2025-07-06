# import tkinter library
import tkinter as tk

# build app
def build_app():
    # create a window
    window = tk.Tk()
    # set window title
    window.title("Tkinter App")
    # set window size
    window.geometry("400x300")
    # run app
    window.mainloop()

if __name__ == "__main__":
    build_app()
# This code creates a simple Tkinter application with a window titled "Tkinter App" and a size of 400x300 pixels.
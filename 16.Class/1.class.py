# import tkinter library
import tkinter as tk
from tkinter import ttk

# create App class
class App(tk.Tk):
    # main setup: App
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])
    
        # Main menu
        self.menu = Menu(self)
        self.main = Main(self)
    
    
class Menu(ttk.Frame):
    # main setup: Menu
    def __init__(self, parent):
        super().__init__(parent)
        # ttk.Label(self, background="#949cf1").pack(expand=True, fill="both")
        self.place(x=0, y=0, relwidth=0.3, relheight=1)
        
        self.create_widgets()
        self.create_layout()
    
    def create_widgets(self):
        self.btn1 = ttk.Button(self, text="button-1")
        self.btn2 = ttk.Button(self, text="button-2")
        self.btn3 = ttk.Button(self, text="button-3")
        
        self.scl1 = ttk.Scale(self, orient="vertical")
        self.scl2 = ttk.Scale(self, orient="vertical")
        
        self.tgl_frm = ttk.Frame(self)
        self.chk1 = ttk.Checkbutton(self.tgl_frm, text="check btn-1")
        self.chk2 = ttk.Checkbutton(self.tgl_frm, text="check btn-2")
        
        self.eny = ttk.Entry(self)
    
    def create_layout(self):
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")
        self.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")
        
        self.btn1.grid(row=0, column=0, sticky="nswe", columnspan=2)
        self.btn2.grid(row=0, column=2, sticky="nswe")
        self.btn3.grid(row=1, column=0, sticky="nswe", columnspan=3)
        
        self.scl1.grid(row=2, column=0, rowspan=2, sticky="nswe", pady=20)
        self.scl2.grid(row=2, column=2, rowspan=2, sticky="nswe", pady=20)
        
        self.tgl_frm.grid(row=4, column=0, columnspan=3, sticky="nswe")
        self.chk1.pack(side="left", expand=True)
        self.chk2.pack(side="left", expand=True)
        
        self.eny.place(relx=0.5, rely=0.95, relwidth=0.9, anchor="center")

class Main(ttk.Frame):
    # Main setup: Main contact
    def __init__(self, parent):
        super().__init__(parent)
        self.place(relx=0.3, y=0, relwidth=0.7, relheight=1)
        
        self.create_widgets()
        self.create_layout()
    
    def create_widgets(self):
        self.tgl_frm1 = ttk.Frame(self)
        self.lbl1 = ttk.Label(self.tgl_frm1, text="Label-1", background="#cfcf12")
        self.btn1 = ttk.Button(self.tgl_frm1, text="Button-1")
        
        self.tgl_frm2 = ttk.Frame(self)
        self.lbl2 = ttk.Label(self.tgl_frm2, text="Label-2", background="#12cf12")
        self.btn2 = ttk.Button(self.tgl_frm2, text="Button-2")
        
    def create_layout(self):
        self.tgl_frm1.pack(side="left", expand=True, fill="both", padx=20, pady=20)
        self.lbl1.pack(expand=True, fill="both", pady=10)
        self.btn1.pack(expand=True, fill="both", pady=10)
        
        self.tgl_frm2.pack(side="left", expand=True, fill="both", padx=20, pady=20)
        self.lbl2.pack(expand=True, fill="both", pady=10)
        self.btn2.pack(expand=True, fill="both", pady=10)

if __name__ == "__main__":
    app = App("Tkinter App (Class)", (600,600))
    app.mainloop()
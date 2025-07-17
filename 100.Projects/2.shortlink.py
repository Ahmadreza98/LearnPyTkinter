import tkinter as tk
from tkinter import ttk
import pyshorteners

class Short_link(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Short Link")
        self.geometry("300x200")
        self.resizable(False, False)
        
        self.set_widgets()
        self.set_layout()
        
    def set_widgets(self):
        self.frm = ttk.Frame(self)
        
        self.link_long_url = tk.StringVar()
        self.lbl_long_url = ttk.Label(self.frm, text="Enter Long URL:",
                                      font=("Arial", 14, "bold"))
        self.eny_long_url = ttk.Entry(self.frm, width=50,
                                      textvariable=self.link_long_url)
        
        self.link_short_url = tk.StringVar()
        self.lbl_short_url = ttk.Label(self.frm, text="Generate Short URL:",
                                     font=("Arial", 14, "bold"))
        self.eny_short_url = ttk.Entry(self.frm, width=50,
                                       textvariable=self.link_short_url)
        
        self.btn = ttk.Button(self.frm, text="Generate!", width=50,
                              command= self.shortern_link_generator)
    
    def set_layout(self):
        self.frm.pack(side="top", expand=True, fill="both")
        
        self.lbl_long_url.pack(pady=10)
        self.eny_long_url.pack()
        
        self.lbl_short_url.pack(pady=10)
        self.eny_short_url.pack()
        
        self.btn.pack(pady=10, side="bottom")

    def shortern_link_generator(self):
        shortener = pyshorteners.Shortener()
        link_short = shortener.tinyurl.short(self.link_long_url.get())
        self.link_short_url.set(value=link_short)


if __name__ == "__main__":
    app = Short_link()
    app.mainloop()
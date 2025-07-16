import os
import logging
import tkinter as tk
from tkinter import ttk
from datetime import datetime

class LoginGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Page")
        self.geometry("290x300")
        self.minsize(290,300)
        self.maxsize(290,300)
        self.configure(bg="#333333")
        
        self.set_style()
        self.set_widgets()
        self.set_layout()

    def set_style(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Custom.TFrame", background="#333333")
        style.configure("Custom.TLabel", background="#333333",foreground="white")
        style.configure("Custom.TButton",font=("Arial","10","bold"))
    
    def set_widgets(self):
        self.tgl_frm = ttk.Frame(self, style="Custom.TFrame")
        
        self.lbl_title = ttk.Label(self.tgl_frm, text="Login", font=("Arial", 20, "bold"), style="Custom.TLabel")
        
        self.lbl_user = ttk.Label(self.tgl_frm, text="Username:", font=("Arial", 12), style="Custom.TLabel")
        self.lbl_pass = ttk.Label(self.tgl_frm, text="Password:", font=("Arial", 12), style="Custom.TLabel")
        
        var_user = tk.StringVar(value="Username")
        var_pass = tk.StringVar(value="Password")
        
        self.eny_user = ttk.Entry(self.tgl_frm, width=25, textvariable= var_user)
        self.eny_pass = ttk.Entry(self.tgl_frm, width=25, show="*", textvariable= var_pass)
        
        self.btn = ttk.Button(self.tgl_frm, text="Login", style="Custom.TButton", command=lambda: self.validate_login(var_user.get(), var_pass.get()))

    def set_layout(self):
        self.lbl_title.grid(row=0, column=0, columnspan=2, pady=40)
        
        self.lbl_user.grid(row=1, column=0)
        self.eny_user.grid(row=1, column=1, pady=20)

        self.lbl_pass.grid(row=2, column=0)
        self.eny_pass.grid(row=2, column=1, pady=20)
        
        self.btn.grid(row=3, column=0, columnspan=2, pady=10)
        
        self.tgl_frm.pack()
    
    def validate_login(self,inp_user, inp_pass):
        if inp_user == "Username" and inp_pass == "Password":
            print(f"Welcome, {inp_user}.")
            self.logging_file((1,inp_user,inp_pass))
        else:
            print("Username or Password is incorrect.")
            self.logging_file((0,inp_user,inp_pass))
            
    def logging_file(self, data):
        script_dir = os.path.dirname(os.path.abspath(__file__))

        log_dir = os.path.join(script_dir, 'logs')
        os.makedirs(log_dir, exist_ok=True)
        
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        log_filename = os.path.join(log_dir, f'app_{timestamp}.log')

        logging.basicConfig(
            filename=log_filename,
            filemode='w',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        if data[0] == 1:
            logging.info(f'Login Successfully, _u:{data[1]}.')
        elif data[0] == 0:
            logging.error(f"Login Failed, _u:{data[1]}, _p:{data[2]}")


        
        
        
        
if __name__ == "__main__":
    app = LoginGUI()
    app.mainloop()
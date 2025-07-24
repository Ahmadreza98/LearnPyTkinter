import tkinter as tk
from tkinter import ttk
import sqlite3
import os

class Personal_information(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Personal Information")
        self.geometry("550x400")
        self.resizable(False, False)
        
        # string variables
        self.str_var_fname = tk.StringVar()
        self.str_var_lname = tk.StringVar()
        self.str_var_gender = tk.StringVar()
        self.str_var_countries = tk.StringVar()
        self.str_var_email = tk.StringVar()
        self.str_var_username = tk.StringVar()
        self.str_var_password = tk.StringVar()
        
        # integer variables
        self.int_var_id_number = tk.IntVar()
        self.int_var_age = tk.IntVar()
        self.int_var_completed_courses = tk.IntVar()
        self.int_var_semester = tk.IntVar()
        
        self.set_widgets()
        self.set_layout()
    
    def set_widgets(self):
        self.main_frm = ttk.Frame(self)
        
        # Top Frame
        self.top_frm = ttk.LabelFrame(self.main_frm, text="User Information")
        
        self.lbl_fname = ttk.Label(self.top_frm, text="First Name")
        self.lbl_lname = ttk.Label(self.top_frm, text="Last Name")
        self.lbl_gender = ttk.Label(self.top_frm, text="Gender")
        self.lbl_age = ttk.Label(self.top_frm, text="Age")
        self.lbl_id = ttk.Label(self.top_frm, text="ID Number")
        self.lbl_countries = ttk.Label(self.top_frm, text="Country")
        
        self.eny_fname = ttk.Entry(self.top_frm, textvariable=self.str_var_fname)
        self.eny_lname = ttk.Entry(self.top_frm, textvariable=self.str_var_lname)
        
        self.spn_age = ttk.Spinbox(self.top_frm, from_=0, to=100, textvariable=self.int_var_age)
        self.spn_id = ttk.Spinbox(self.top_frm, from_=0, to=9999999999, textvariable=self.int_var_id_number)
        
        self.com_gender = ttk.Combobox(self.top_frm,values=["", "Mr.", "Ms.","Other."], textvariable=self.str_var_gender)
        self.com_countries = ttk.Combobox(self.top_frm, values=((''),
    ('AFGHANISTAN'),
    ('ALBANIA'),
    ('ALGERIA'),
    ('ANDORRA'),
    ('ANGOLA'),
    ('ANGUILLA'),
    ('ANTARCTICA'),
    ('ARGENTINA'),
    ('ARMENIA'),
    ('ARUBA'),
    ('AUSTRALIA'),
    ('AUSTRIA'),
    ('AZERBAIJAN'),
    ('BAHAMAS'),
    ('BAHRAIN'),
    ('BANGLADESH'),
    ('BARBADOS'),
    ('BELARUS'),
    ('BELGIUM'),
    ('BELIZE'),
    ('BENIN'),
    ('BERMUDA'),
    ('BHUTAN'),
    ('BOLIVIA'),
    ('BOTSWANA'),
), textvariable=self.str_var_countries)
        
        # Middle-1 Frame
        self.mid_1_frm = ttk.Labelframe(self.main_frm, text="Register")
        
        self.lbl_email = ttk.Label(self.mid_1_frm, text="Email Address")
        self.lbl_username = ttk.Label(self.mid_1_frm, text="Username")
        self.lbl_password = ttk.Label(self.mid_1_frm, text="Password")
        
        self.eny_email = ttk.Entry(self.mid_1_frm, textvariable=self.str_var_email)
        self.eny_username = ttk.Entry(self.mid_1_frm, textvariable=self.str_var_username)
        self.eny_password = ttk.Entry(self.mid_1_frm, show="*", textvariable=self.str_var_password)
        
        self.chk_show_password = ttk.Checkbutton(self.mid_1_frm, text="Show password")
        
        # Middle-2 Frame
        self.mid_2_frm = ttk.Labelframe(self.main_frm)
        
        self.lbl_registration_status = ttk.Label(self.mid_2_frm, text="Registration Status")
        self.lbl_completed_courses = ttk.Label(self.mid_2_frm, text="# Completed Courses")
        self.lbl_semesters = ttk.Label(self.mid_2_frm, text="# Semesters")
        
        self.spn_completed_courses = ttk.Spinbox(self.mid_2_frm, from_=0, to=20, textvariable=self.int_var_completed_courses)
        self.spn_semesters = ttk.Spinbox(self.mid_2_frm, from_=0, to=14, textvariable=self.int_var_semester)
        
        self.chk_registration_status = ttk.Checkbutton(self.mid_2_frm, text="Currently, Registered")
        
        # Bottom Frame
        self.btm_frm = ttk.Labelframe(self.main_frm, text="Terms & Conditions")
        
        self.chk_terms_and_conditions = ttk.Checkbutton(self.btm_frm,text="I Accept The Terms & Conditions.")
        
        # Save and Export Button
        self.btn_frm = ttk.Frame(self.main_frm)
        
        self.btn_save = ttk.Button(self.btn_frm, text="Save", command= self.button_save)
        self.btn_export = ttk.Button(self.btn_frm, text="Export", command=lambda: print("Export!"))
        
        
    def set_layout(self):
        # main layout
        self.main_frm.pack()
        
        # top layout
        self.top_frm.pack(side="top", padx=10, pady=5)
        
        self.lbl_fname.grid(row=0, column=0)
        self.lbl_lname.grid(row=0, column=1)
        self.lbl_gender.grid(row=0, column=2)
        self.lbl_id.grid(row=2, column=0)
        self.lbl_age.grid(row=2, column=1)
        self.lbl_countries.grid(row=2,column=2)
        
        self.eny_fname.grid(row=1, column=0, padx=10, pady=5)
        self.eny_lname.grid(row=1, column=1, padx=10, pady=5)
        
        self.spn_id.grid(row=3, column=0, padx=10, pady=5)
        self.spn_age.grid(row=3, column=1, padx=10, pady=5)
        
        self.com_gender.grid(row=1, column=2, padx=10, pady=5)
        self.com_countries.grid(row=3, column=2, padx=10, pady=5)
        
        # middle-2 layout
        self.mid_2_frm.pack(side="top",padx=10, pady=5)
        
        self.lbl_registration_status.grid(row=0, column=0)
        self.lbl_completed_courses.grid(row=0, column=1)
        self.lbl_semesters.grid(row=0, column=2)
        
        self.chk_registration_status.grid(row=1, column=0, padx=12, pady=5)
        self.spn_completed_courses.grid(row=1, column=1, padx=12, pady=5)
        self.spn_semesters.grid(row=1, column=2, padx=11, pady=5)
        
        # middle-1 layout
        self.mid_1_frm.pack(side="top",padx=10, pady=5)
        
        self.lbl_email.grid(row=0, column=0)
        self.lbl_username.grid(row=0, column=1)
        self.lbl_password.grid(row=0, column=2)
        
        self.eny_email.grid(row=1, column=0, padx=17, pady=5)
        self.eny_username.grid(row=1, column=1, padx=17, pady=5)
        self.eny_password.grid(row=1, column=2, padx=18, pady=5)
        
        self.chk_show_password.grid(row=2, column=2)
        
        # bottom layout
        self.btm_frm.pack(side="top", padx=10, pady=5, fill="x", expand=True)
        
        self.chk_terms_and_conditions.grid(row=0, column=0)
        
        # save & export layout
        self.btn_frm.pack(side="top", fill="x", expand=True, padx=10, pady=5)
        self.btn_save.pack(side="right", padx=5)
        # self.btn_export.pack(side="right", padx=5)
    
    def button_save(self):
        folder_path = os.path.join(os.getcwd(), "database")
        os.makedirs(folder_path, exist_ok=True)
        db_path = os.path.join(folder_path, "personal_information.db")
        
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        QUERY = """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                gender TEXT NOT NULL,
                countries TEXT NOT NULL,
                id_number INTEGER NOT NULL,
                age INTEGER NOT NULL,
                email TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )
        """
        INSERT = """
            INSERT INTO users (first_name, last_name, gender, countries, id_number, age, email, username, password) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?) 
        """
        cursor.execute(QUERY)
        cursor.execute(INSERT, (self.str_var_fname.get(), self.str_var_lname.get(), self.str_var_gender.get(), self.str_var_countries.get(), self.int_var_id_number.get(), self.int_var_age.get(), self.str_var_email.get(), self.str_var_username.get(), self.str_var_password.get()))
        
        conn.commit()
        conn.close()
        
        self.eny_fname.delete(0, tk.END)
        self.eny_email.delete(0, tk.END)
        self.eny_lname.delete(0, tk.END)
        self.eny_password.delete(0, tk.END)
        self.eny_username.delete(0, tk.END)
        
        self.spn_age.delete(0, tk.END)
        self.spn_completed_courses.delete(0, tk.END)
        self.spn_id.delete(0, tk.END)
        self.spn_semesters.delete(0, tk.END)
        
        self.com_gender.delete(0, tk.END)
        self.com_countries.delete(0, tk.END)
        
        print("Data Saved.")
        
    

if __name__ == "__main__":
    app = Personal_information()
    app.mainloop()
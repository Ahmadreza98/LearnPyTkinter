import tkinter as tk
from tkinter import ttk
import openpyxl

class EditExcelApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Edit Excel File")
        # self.geometry("600x300")
        
        self.style = ttk.Style()
        
        # define text variable
        self.txt_var_sub = tk.BooleanVar()
        self.txt_var_md = tk.BooleanVar()
        
        # Call the method to set the theme
        self.call("source", "./101.Exam/forest-light.tcl")
        self.call("source", "./101.Exam/forest-dark.tcl")
        
        self.style.theme_use("forest-dark")

        self.main_frm = ttk.Frame(self)
        self.main_frm.pack(fill=tk.BOTH, expand=True)
        
        self.cols = ["Name", "Age", "Subscription", "Employment"]
        
        self.lft_frm_func()  # Create left frame
        self.rht_frm_func()  # Create right frame
        self.set_attributes()
        self.layouts()
        
        self.load_data()
    
    def lft_frm_func(self):
        self.lft_frm = ttk.Labelframe(self.main_frm, text="Insert Row")
        self.eny_name = ttk.Entry(self.lft_frm)
        self.spn_age = ttk.Spinbox(self.lft_frm, from_=18, to=100)
        self.com_subscribed = ttk.Combobox(self.lft_frm, values=["Subscribed", "Not Subscribed", "Other"])
        self.chk_employed = ttk.Checkbutton(self.lft_frm, text="Employed", variable=self.txt_var_sub)
        self.btn_insert = ttk.Button(self.lft_frm, text="Insert", command=self.insert_data)
        self.sep = ttk.Separator(self.lft_frm)
        self.chk_mode = ttk.Checkbutton(self.lft_frm, text="Mode", command=self.toggle_mode, style="Switch")
    
    def toggle_mode(self):
        if self.chk_mode.instate(["selected"]):
            self.style.theme_use("forest-light")
        else:
            self.style.theme_use("forest-dark")
    
    def insert_data(self):

        self.trv_excel.insert("",tk.END, values=(self.eny_name.get(), self.spn_age.get(), self.com_subscribed.get(), "Employed" if self.txt_var_sub.get() else "Unemployed"))
        
    def rht_frm_func(self):
        self.rht_frm = ttk.Frame(self.main_frm)
        
        self.trv_scroll = ttk.Scrollbar(self.rht_frm)
        
        self.trv_excel = ttk.Treeview(self.rht_frm, show="headings", columns=self.cols, height=11, yscrollcommand=self.trv_scroll.set)
        
        self.trv_excel.column("Name", width=100)
        self.trv_excel.column("Age", width=50)
        self.trv_excel.column("Subscription", width=100)
        self.trv_excel.column("Employment", width=100)
        
    
    def set_attributes(self):
        self.eny_name.insert(0,"Name")
        self.eny_name.bind("<FocusIn>", lambda e: self.eny_name.delete(0, tk.END))
        
        self.spn_age.insert(0, "Age")
        self.spn_age.bind("<FocusIn>", lambda e: self.spn_age.delete(0, tk.END))
        
        self.com_subscribed.insert(0, "Subscribed")
        
        self.trv_scroll.configure(command=self.trv_excel.yview)
        
    
    def layouts(self):
        # Left Frame
        self.lft_frm.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")
        
        self.eny_name.grid(row=0, column=0, padx=5, pady=(0, 5), sticky="ew")
        self.spn_age.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        self.com_subscribed.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
        self.chk_employed.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
        self.btn_insert.grid(row=4, column=0, padx=5, pady=5, sticky="ew")
        self.sep.grid(row=5, column=0, padx=(20, 10), pady=10, sticky="ew")
        self.chk_mode.grid(row=6, column=0, padx=5, pady=10, sticky="news")
        
        # Right Frame
        self.rht_frm.grid(row=0, column=1, pady=10, sticky="nsew")
        self.trv_scroll.pack(side="right", fill="y")
        self.trv_excel.pack()
    
    def load_data(self):
        PATH_EXECL = "./101.Exam/people.xlsx"
        workbook = openpyxl.load_workbook(PATH_EXECL)
        select_sheet = workbook.active
        
        list_values = list(select_sheet.values)
        
        for col_name in list_values[0]:
            self.trv_excel.heading(col_name, text=col_name)
        
        for col_tuple in list_values[1:]:
            self.trv_excel.insert("", tk.END, values=col_tuple)



if __name__ == "__main__":
    app = EditExcelApp()
    app.mainloop()
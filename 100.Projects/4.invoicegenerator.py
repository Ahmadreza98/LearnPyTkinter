from datetime import datetime
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from docxtpl import DocxTemplate
import re


class Invoice(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Invoice Generator")
        self.geometry("780x550")
        self.resizable(False, False)
        
        self.add_device()
        self.tree_view()
        self.btn_generator_invoice()
        self.set_layout()
        
    
    def add_device(self):
        self.info_frm = ttk.Frame(self)
        
        self.lbl_litter_head_number = ttk.Label(self.info_frm, text="Litter Head Number")
        self.lbl_date = ttk.Label(self.info_frm, text="Date")
        self.lbl_name_client = ttk.Label(self.info_frm, text="Name Client")
        self.lbl_name_company = ttk.Label(self.info_frm, text="Name Company")
        self.lbl_street_address = ttk.Label(self.info_frm, text="Street Address")
        self.lbl_city = ttk.Label(self.info_frm, text="City")
        self.lbl_state_abbv = ttk.Label(self.info_frm, text="State Abbv")
        self.lbl_zip_code = ttk.Label(self.info_frm, text="Zip Code")
        self.lbl_phone_number = ttk.Label(self.info_frm, text="Phone Number")
        self.lbl_sales_person = ttk.Label(self.info_frm, text="Sales Person")
        self.lbl_post_number = ttk.Label(self.info_frm, text="Post Number")
        self.lbl_requisitioner = ttk.Label(self.info_frm, text="Requisitioner")
        self.lbl_shipped_via = ttk.Label(self.info_frm, text="Shipped Via")
        self.lbl_fob_point = ttk.Label(self.info_frm, text="F.O.B Point")
        self.lbl_terms = ttk.Label(self.info_frm, text="Terms")
        self.lbl_quantity = ttk.Label(self.info_frm, text="Quantity")
        self.lbl_description = ttk.Label(self.info_frm, text="Description")
        self.lbl_unit_price = ttk.Label(self.info_frm, text="Unit Price")
        self.lbl_sales_tax = ttk.Label(self.info_frm, text="Sales Tax (%)")
        self.lbl_shipping_and_handing = ttk.Label(self.info_frm, text="Shipping & Handing")
        
        self.eny_litter_head_number = ttk.Entry(self.info_frm)
        self.eny_date = DateEntry(self.info_frm, width=17, date_pattern='dd/mm/yyyy')
        self.eny_name_client = ttk.Entry(self.info_frm)
        self.eny_name_company = ttk.Entry(self.info_frm)
        self.eny_street_address = ttk.Entry(self.info_frm)
        self.eny_city = ttk.Entry(self.info_frm)
        self.eny_state_abbv = ttk.Entry(self.info_frm)
        self.eny_zip_code = ttk.Entry(self.info_frm)
        self.eny_phone_number = ttk.Entry(self.info_frm)
        self.eny_sales_person = ttk.Entry(self.info_frm)
        self.eny_post_number = ttk.Entry(self.info_frm)
        self.eny_requisitioner = ttk.Entry(self.info_frm)
        self.eny_shipped_via = ttk.Entry(self.info_frm)
        self.eny_fob_point = ttk.Entry(self.info_frm)
        self.eny_terms = ttk.Entry(self.info_frm)
        self.eny_quantity = ttk.Entry(self.info_frm)
        self.eny_description = ttk.Entry(self.info_frm)
        self.eny_unit_price = ttk.Entry(self.info_frm)
        self.com_sales_tax = ttk.Combobox(self.info_frm,values=("Selected", "10", "15", "20", "25"), width=17)
        self.eny_shipping_and_handing = ttk.Entry(self.info_frm)
        
        self.btn_add_item = ttk.Button(self.info_frm, text="Add Item", command=self.btn_add_item, width=18)
        
    def tree_view(self):
        self.tbl_frm = ttk.Frame(self)
        
        name_cols = ("Quantity","Description","Unit Price","Total","Shipping & Handing")
        
        # scroll bar
        y_scroll = ttk.Scrollbar(self.tbl_frm, orient="vertical")
        
        self.trv = ttk.Treeview(self.tbl_frm, columns=name_cols, show="headings", height=10,
            yscrollcommand=y_scroll.set)
        
        # configure scroll bars
        y_scroll.config(command=self.trv.yview)
        y_scroll.grid(row=0, column=1, sticky="ns")

        # frame resize settings
        self.tbl_frm.rowconfigure(0, weight=1)
        self.tbl_frm.columnconfigure(0, weight=1)

        # add headings
        for col in name_cols:
            self.trv.heading(col, text=col)
            self.trv.column(col, width=80, anchor="center")
            
    
    def btn_generator_invoice(self):
        self.btn_frm = ttk.Frame(self)
        
        self.btn_gen_invoice = ttk.Button(self.btn_frm, text="Generate Invoice", command=self.generate_invoice)
        self.btn_new_gen_invoice = ttk.Button(self.btn_frm, text="New Invoice")
    
    def set_layout(self):
        # main layout
        self.info_frm.pack(side="top",fill="both", expand=True, pady=5)
        self.tbl_frm.pack(side="top",fill="both", expand=True,padx=10, pady=5)
        self.btn_frm.pack(side="top",fill="both", expand=True, pady=10)
        
        # First Row Labels
        self.lbl_litter_head_number.grid(row=0, column=0, padx=10, pady=5)
        self.lbl_date.grid(row=0, column=1, padx=10, pady=5)
        self.lbl_name_client.grid(row=0, column=2, padx=10, pady=5)
        self.lbl_name_company.grid(row=0, column=3, padx=10, pady=5)
        self.lbl_street_address.grid(row=0, column=4, padx=10, pady=5)
        
        # Second Row Labels
        self.lbl_city.grid(row=2, column=0, padx=15)
        self.lbl_state_abbv.grid(row=2, column=1, padx=15)
        self.lbl_zip_code.grid(row=2, column=2, padx=15)
        self.lbl_phone_number.grid(row=2, column=3, padx=15)
        self.lbl_sales_person.grid(row=2, column=4, padx=15)
        
        # Third Row Labels
        self.lbl_post_number.grid(row=4, column=0, padx=15)
        self.lbl_requisitioner.grid(row=4, column=1, padx=15)
        self.lbl_shipped_via.grid(row=4, column=2, padx=15)
        self.lbl_fob_point.grid(row=4, column=3, padx=15)
        self.lbl_terms.grid(row=4, column=4, padx=15)
        
        # Fourth Row Labels
        self.lbl_quantity.grid(row=6, column=0, padx=15)
        self.lbl_description.grid(row=6, column=1, padx=15)
        self.lbl_unit_price.grid(row=6, column=2, padx=15)
        self.lbl_sales_tax.grid(row=6, column=3, padx=5)
        self.lbl_shipping_and_handing.grid(row=6, column=4, padx=5)
        
        # First Row Entries
        self.eny_litter_head_number.grid(row=1, column=0, padx=15)
        self.eny_date.grid(row=1, column=1, padx=15)
        self.eny_name_client.grid(row=1, column=2, padx=15)
        self.eny_name_company.grid(row=1, column=3, padx=15)
        self.eny_street_address.grid(row=1, column=4, padx=15)
        
        # Second Row Entries
        self.eny_city.grid(row=3, column=0, padx=15)
        self.eny_state_abbv.grid(row=3, column=1, padx=15)
        self.eny_zip_code.grid(row=3, column=2, padx=15)
        self.eny_phone_number.grid(row=3, column=3, padx=15)
        self.eny_sales_person.grid(row=3, column=4, padx=15)
        
        # Third Row Entries
        self.eny_post_number.grid(row=5, column=0, padx=15)
        self.eny_requisitioner.grid(row=5, column=1, padx=15)
        self.eny_shipped_via.grid(row=5, column=2, padx=15)
        self.eny_fob_point.grid(row=5, column=3, padx=15)
        self.eny_terms.grid(row=5, column=4, padx=15)
        
        # Fourth Row Entries
        self.eny_quantity.grid(row=7, column=0, padx=15)
        self.eny_description.grid(row=7, column=1, padx=15)
        self.eny_unit_price.grid(row=7, column=2, padx=15)
        self.com_sales_tax.grid(row=7, column=3, padx=15)
        self.eny_shipping_and_handing.grid(row=7, column=4, padx=15)
        
        self.btn_add_item.grid(row=8, column=0, padx=15, pady=10, columnspan=5)
        
        # Treeview setup
        self.trv.grid(row=0, column=0, sticky="nsew",padx=5, pady=5)
        
        # generate invoice buttons
        self.btn_gen_invoice.grid(row=0, column=3, padx=10, pady=5)
        self.btn_new_gen_invoice.grid(row=0, column=4, padx=10, pady=5)
    
    def btn_add_item(self):
        qty = int(self.eny_quantity.get())
        des = self.eny_description.get()
        unit_price = float(self.eny_unit_price.get())
        total = qty * unit_price
        shipping_and_handing = 1 * int(self.eny_shipping_and_handing.get())
        
        self.trv.insert("", "end", values=(qty, des, f'${unit_price}', f'${total}', f'${shipping_and_handing}'))
    
    
    def generate_invoice(self):
        
        docx = DocxTemplate("./100.Projects/extra_files/Sales_invoice.docx")
               
        contexts = {
            "litter_head_number": self.eny_litter_head_number.get(),
            "date": self.eny_date.get(),
            "name_client": self.eny_name_client.get(),
            "name_company": self.eny_name_company.get(),
            "street_address": self.eny_street_address.get(),
            "city": self.eny_city.get(),
            "state_abbv": self.eny_state_abbv.get(),
            "zip_code": self.eny_zip_code.get(),
            "phone_number": self.eny_phone_number.get(),
            "sales_person": self.eny_sales_person.get(),
            "post_number": self.eny_post_number.get(),
            "requisitioner": self.eny_requisitioner.get(),
            "shipped_via": self.eny_shipped_via.get(),
            "fob_point": self.eny_fob_point.get(),
            "terms": self.eny_terms.get(),
            "items": [self.trv.item(child)["values"][0:4] for child in self.trv.get_children()],
            "sub_total": f"${sum([float(re.search(r"\d+(\.\d+)?", self.trv.item(child)["values"][3]).group(0)) for child in self.trv.get_children()])}",
            "sales_tax": f"${float(self.com_sales_tax.get())/100 * sum([float(re.search(r"\d+(\.\d+)?", self.trv.item(child)["values"][3]).group(0)) for child in self.trv.get_children()])}",
            "ship_hand": f"${sum([float(re.search(r"\d+(\.\d+)?", self.trv.item(child)["values"][4]).group(0)) for child in self.trv.get_children()])}",
            "total_due": f"${sum([float(re.search(r"\d+(\.\d+)?", self.trv.item(child)["values"][3]).group(0)) for child in self.trv.get_children()]) + float(self.com_sales_tax.get())/100 * sum([float(re.search(r"\d+(\.\d+)?", self.trv.item(child)["values"][3]).group(0)) for child in self.trv.get_children()]) + sum([float(re.search(r"\d+(\.\d+)?", self.trv.item(child)["values"][4]).group(0)) for child in self.trv.get_children()])}"
        }
        print(contexts)
        docx.render(contexts)
        
        docx.save(f"./100.Projects/extra_files/invoice_{self.eny_name_company.get()}_{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.docx")
    

if __name__ == "__main__":
    app = Invoice()
    app.mainloop()
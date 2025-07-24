import customtkinter as ctk

class Daily_task(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("Daily Task Manager")
        self.resizable(False, False)
        
        
        self.set_widgets()
        self.set_layout()
        
    # add widgets to app
    def set_widgets(self):
            self.lbl_title = ctk.CTkLabel(self, text="Daily Task Manager", font=ctk.CTkFont(size=30, weight="bold", family="Fira Code"))
            self.eny_task = ctk.CTkEntry(self, placeholder_text="Enter New Task", width=300, font=ctk.CTkFont(size=15, family="Fira Code", weight="bold"))
            self.btn_add_task = ctk.CTkButton(self, text="Add Task", command=self.add_task, width=100, font=ctk.CTkFont(size=15, family="Fira Code", weight="bold"))
            
            # right frame
            self.hrt_frm = ctk.CTkFrame(self, width=200, height=500, corner_radius=5)
            self.lbl_rht_sub_title = ctk.CTkLabel(self.hrt_frm, text="Doing", font=ctk.CTkFont(size=20, weight="bold", family="Fira Code"))
        
    def set_layout(self):
            self.lbl_title.pack(pady=20)
            self.eny_task.pack(side="top", fill="x", padx=10, pady=10)
            self.btn_add_task.pack(side="top", fill="x", padx=10, pady=10)
            
            self.hrt_frm.pack(side="top", fill="both", padx=10, pady=10)
            
            self.lbl_rht_sub_title.pack(side="top", padx=100, pady=20)
            
    def add_task(self):
        if self.eny_task.get() != "":
            self.chk_task = ctk.CTkCheckBox(self.hrt_frm, text=self.eny_task.get(), font=ctk.CTkFont(size=15, family="Fira Code", weight="bold"))
            self.chk_task.pack(side="top", fill="x", padx=10, pady=5)
            self.eny_task.delete(0, 'end')
    
        

# Run the app
if __name__ == "__main__":
    app = Daily_task()
    app.mainloop()

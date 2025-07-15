import tkinter as tk
from tkinter import ttk

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Form")
        self.root.geometry("400x200")
        self.root.resizable(True, False)

        # Configure grid weights for responsiveness
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=2)

        self.create_widgets()

    def create_widgets(self):
        # Username Label and Entry
        ttk.Label(self.root, text="Username:").grid(
            row=0, column=0, sticky="e", padx=10, pady=10
        )
        self.username_entry = ttk.Entry(self.root)
        self.username_entry.grid(
            row=0, column=1, sticky="ew", padx=10, pady=10
        )

        # Password Label and Entry
        ttk.Label(self.root, text="Password:").grid(
            row=1, column=0, sticky="e", padx=10, pady=10
        )
        self.password_entry = ttk.Entry(self.root, show="*")
        self.password_entry.grid(
            row=1, column=1, sticky="ew", padx=10, pady=10
        )

        # Remember me Checkbox
        self.remember_var = tk.BooleanVar()
        self.remember_check = ttk.Checkbutton(
            self.root, text="Remember me", variable=self.remember_var
        )
        self.remember_check.grid(
            row=2, column=1, sticky="w", padx=10, pady=(0, 10)
        )

        # Login Button
        login_btn = ttk.Button(self.root, text="Login", command=self.login)
        login_btn.grid(row=3, column=1, sticky="e", padx=10, pady=(0, 10))

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        remember = self.remember_var.get()
        print(f"Username: {username}, Password: {password}, Remember: {remember}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()

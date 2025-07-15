# import tkinter library
import tkinter as tk
from tkinter import ttk

# build_app function
def build_app():

    # Main application window
    window = tk.Tk()
    window.title("Pack Layout")
    window.geometry("500x300")
    window.configure(padx=10, pady=10)

    # ==== Top Frame: Header ====
    header_frame = ttk.Frame(window, padding=10)
    header_frame.pack(side="top", fill="x")

    header_label = ttk.Label(header_frame, text="Welcome to My App", font=("Arial", 16, "bold"))
    header_label.pack()

    # ==== Center Frame: Content Area ====
    content_frame = ttk.Frame(window, padding=10)
    content_frame.pack(side="top", fill="both", expand=True)

    left_panel = ttk.Frame(content_frame)
    left_panel.pack(side="left", fill="y")

    right_panel = ttk.Frame(content_frame)
    right_panel.pack(side="right", fill="both", expand=True)

    # Left panel: Navigation
    ttk.Label(left_panel, text="Menu", font=("Arial", 12, "underline")).pack(pady=(0, 10))
    ttk.Button(left_panel, text="Home").pack(fill="x", pady=2)
    ttk.Button(left_panel, text="Settings").pack(fill="x", pady=2)
    ttk.Button(left_panel, text="About").pack(fill="x", pady=2)

    # Right panel: Content
    ttk.Label(right_panel, text="Main Content Area", font=("Arial", 12, "bold")).pack(pady=(0, 10))
    ttk.Label(right_panel, wraplength=300,
            text="This is a professional example showing how to organize widgets using "
                "`pack()` with frames, sides, fills, and expands.").pack()

    # ==== Bottom Frame: Footer ====
    footer_frame = ttk.Frame(window, padding=10)
    footer_frame.pack(side="bottom", fill="x")

    ttk.Button(footer_frame, text="Exit", command=window.destroy).pack(side="right")

    # Start the main loop
    window.mainloop()

if __name__ == "__main__":
    build_app()
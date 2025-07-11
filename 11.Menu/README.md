## 📜 Menus in Tkinter (With `ttk` GUI)

Menus are created using the **`tk.Menu`** class and can be attached to the root window. You can build:

* A **main menu bar**
* **Dropdown** (cascading) menus
* **Context (right-click)** menus

---

## 🧱 Basic Menu Example

```python
import tkinter as tk
from tkinter import ttk

def say_hello():
    print("Hello!")

root = tk.Tk()
root.title("Menu Example")

# Create the menu bar
menubar = tk.Menu(root)

# Create a File menu
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=say_hello)
file_menu.add_command(label="Open", command=say_hello)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add File menu to the menubar
menubar.add_cascade(label="File", menu=file_menu)

# Set the menu bar
root.config(menu=menubar)

# Add a ttk widget
ttk.Label(root, text="Use the menu above.").pack(pady=20)

root.mainloop()
```

✅ This creates a **File** menu with "New", "Open", and "Exit" options.

---

## 🧰 Menu Methods


| Method                                  | Description                            |
| --------------------------------------- | -------------------------------------- |
| `add_command(label=..., command=...)` | Adds a menu item                       |
| `add_separator()`                     | Adds a line between menu items         |
| `add_cascade(label=..., menu=...)`    | Adds a submenu                         |
| `add_checkbutton(...)`                | Adds a toggle option                   |
| `add_radiobutton(...)`                | Adds a mutually-exclusive option group |

---

## 🧭 Cascading (Sub)Menus

```python
edit_menu = tk.Menu(menubar, tearoff=0)
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

tools_menu = tk.Menu(edit_menu, tearoff=0)
tools_menu.add_command(label="Brush")
tools_menu.add_command(label="Eraser")

edit_menu.add_cascade(label="Tools", menu=tools_menu)

menubar.add_cascade(label="Edit", menu=edit_menu)
```

---

## ⚙️ Checkbuttons & Radiobuttons in Menus

```python
show_line_numbers = tk.BooleanVar()

view_menu = tk.Menu(menubar, tearoff=0)
view_menu.add_checkbutton(label="Show Line Numbers", variable=show_line_numbers)

theme_var = tk.StringVar(value="Light")
view_menu.add_radiobutton(label="Light Theme", variable=theme_var, value="Light")
view_menu.add_radiobutton(label="Dark Theme", variable=theme_var, value="Dark")

menubar.add_cascade(label="View", menu=view_menu)
```

---

## 🖱 Context (Right-Click) Menu

```python
popup = tk.Menu(root, tearoff=0)
popup.add_command(label="Copy")
popup.add_command(label="Paste")

def show_popup(event):
    popup.tk_popup(event.x_root, event.y_root)

root.bind("<Button-3>", show_popup)  # Right-click on Windows/Linux
```

---

## 🎨 Styling Menus

Menus  **do not use `ttk` styling** . You can configure font and colors manually (platform-dependent):

```python
file_menu.configure(font=('Segoe UI', 10))
```

For advanced custom UIs, consider third-party libraries like `TkinterDnD`, `ttkbootstrap`, or `customtkinter`.

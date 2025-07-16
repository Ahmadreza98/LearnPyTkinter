# Tkinter Variables with `ttk`

Tkinter provides special **control variables** that allow you to link widget values to Python variables. This connection makes it easy to read, update, and track the state of widgets.

---

## 🔑 What Are Tkinter Variables?

Tkinter variables are classes like:

- `StringVar()` — stores text strings
- `IntVar()` — stores integers
- `BooleanVar()` — stores True/False
- `DoubleVar()` — stores floating-point numbers

They provide `.get()` and `.set()` methods to access or modify their value.

---

## ⚙️ Why Use Tkinter Variables?

- **Two-way binding:** When the variable changes, the widget updates automatically.
- **Readability:** You can get the widget’s value by reading the variable.
- **Control:** Easily set or reset values programmatically.

---

## 🧩 How to Use Tkinter Variables with `ttk` Widgets

### 1. Associate a Variable with a Widget

Most input widgets support a `textvariable` (or `variable`) option to bind the Tkinter variable.

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

name_var = tk.StringVar()
name_entry = ttk.Entry(root, textvariable=name_var)
name_entry.pack()

age_var = tk.IntVar()
age_spinbox = ttk.Spinbox(root, from_=0, to=100, textvariable=age_var)
age_spinbox.pack()
```

### 2. Getting and Setting the Value

```python
# Set a default value
name_var.set("Alice")

# Get the current value
print(name_var.get())
```

---

## 🧮 Example: Checkbox with `BooleanVar`

```python
agree_var = tk.BooleanVar()
agree_check = ttk.Checkbutton(root, text="I Agree", variable=agree_var)
agree_check.pack()

# Check if checked
if agree_var.get():
    print("User agreed!")
```

---

## 📝 Common Widgets and Their Associated Variables

| Widget          | Variable Type               | Option Name      |
| --------------- | --------------------------- | ---------------- |
| `Entry`       | `StringVar`               | `textvariable` |
| `Combobox`    | `StringVar`               | `textvariable` |
| `Spinbox`     | `IntVar` or `StringVar` | `textvariable` |
| `Checkbutton` | `BooleanVar`              | `variable`     |
| `Radiobutton` | `IntVar` or `StringVar` | `variable`     |
| `Scale`       | `DoubleVar`               | `variable`     |

---

## 💡 Tips

- Always use Tkinter variables for widgets where you want to track or update values easily.
- Avoid mixing direct widget `.get()` calls with variable `.get()`. Use variables if you want better control and binding.

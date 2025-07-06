# Tkinter Widgets with `ttk`

`ttk` stands for **Themed Tkinter Widgets**, providing a more modern and styled look to standard Tkinter widgets.

---

## 🛠 How to Import `ttk`

```python
import tkinter as tk
from tkinter import ttk
```

---

## 📋 List of Common `ttk` Widgets

### 1. **ttk.Label**

Displays text or images.

```python
label = ttk.Label(root, text="Hello, TTK!")
label.pack()
```

### 2. **ttk.Button**

A button that triggers an action.

```python
button = ttk.Button(root, text="Click Me", command=my_function)
button.pack()
```

### 3. **ttk.Entry**

A single-line text entry widget.

```python
entry = ttk.Entry(root)
entry.pack()
```

### 4. **ttk.Combobox**

Dropdown menu for selecting options.

```python
combo = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
combo.pack()
```

### 5. **ttk.Checkbutton**

Checkbox for binary choices.

```python
var = tk.BooleanVar()
check = ttk.Checkbutton(root, text="I agree", variable=var)
check.pack()
```

### 6. **ttk.Radiobutton**

Allows selection of one option from a group.

```python
selected = tk.StringVar()
radio1 = ttk.Radiobutton(root, text="A", variable=selected, value="A")
radio2 = ttk.Radiobutton(root, text="B", variable=selected, value="B")
radio1.pack()
radio2.pack()
```

### 7. **ttk.Scale**

Slider for numeric values.

```python
scale = ttk.Scale(root, from_=0, to=100)
scale.pack()
```

### 8. **ttk.Progressbar**

Visual indicator of progress.

```python
progress = ttk.Progressbar(root, length=200, mode="determinate")
progress["value"] = 50  # 0 to 100
progress.pack()
```

### 9. **ttk.Treeview**

Displays tabular data or hierarchical structures.

```python
tree = ttk.Treeview(root, columns=("Name", "Age"))
tree.heading("#0", text="ID")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.insert("", "end", text="1", values=("Alice", 30))
tree.pack()
```

### 10. **ttk.Notebook**

Tabbed interface.

```python
notebook = ttk.Notebook(root)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.pack()
```

---

## ✅ Summary Table

| Widget          | Description                     |
| --------------- | ------------------------------- |
| `Label`       | Display text or image           |
| `Button`      | Clickable action                |
| `Entry`       | Single-line input               |
| `Combobox`    | Dropdown selector               |
| `Checkbutton` | Binary on/off input             |
| `Radiobutton` | Choose one of many options      |
| `Scale`       | Numeric slider                  |
| `Progressbar` | Show progress visually          |
| `Treeview`    | Table or hierarchical data view |
| `Notebook`    | Tabbed interface                |

---

## 💡 Tip:

You can customize `ttk` styles using the `ttk.Style()` class.

```python
style = ttk.Style()
style.configure("TButton", foreground="blue", padding=10)
```

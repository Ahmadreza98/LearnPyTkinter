# Tkinter `ttk.Treeview` Widget

The `Treeview` widget in Tkinter (from the `ttk` module) is used to display **tabular data** or **hierarchical tree structures**. It is commonly used for file browsers, tables, and nested lists.

---

## 🧱 Import and Create Treeview

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
tree = ttk.Treeview(root)
tree.pack()
```

---

## 🌲 Tree Structure vs Table

- Treeview can be used in **tree mode** (with parent-child relationships).
- It can also be used like a **table**, using columns.

---

## 📁 Adding Items

```python
tree.insert(parent='', index='end', iid='item1', text='Parent Item')
tree.insert(parent='item1', index='end', iid='child1', text='Child Item')
```

- `parent=''`: root level
- `index='end'`: append at the end
- `iid`: unique ID
- `text`: the visible label

---

## 📊 Columns and Headings (Tabular Data)

```python
tree['columns'] = ('name', 'age')
tree.heading('#0', text='ID')
tree.heading('name', text='Name')
tree.heading('age', text='Age')

tree.insert('', 'end', text='1', values=('Alice', 30))
tree.insert('', 'end', text='2', values=('Bob', 25))
```

- `#0` is the default first column (tree column)
- `values=(...)` sets column values (excluding `#0`)

---

## 🎨 Styling and Options

| Option              | Description                    |
| ------------------- | ------------------------------ |
| `show='tree'`     | Only tree column (hide table)  |
| `show='headings'` | Only table, no tree column     |
| `height`          | Number of rows shown           |
| `selectmode`      | `"browse"` or `"extended"` |

---

## 🔍 Accessing Selected Item

```python
selected = tree.selection()
for item in selected:
    print("Item ID:", item)
    print("Values:", tree.item(item, 'values'))
```

---

## 🔁 Modifying and Deleting Items

```python
tree.item('item1', text='Updated Text', values=('New Name', 99))
tree.delete('item1')
```

---

## 🪜 Hierarchical Example

```python
tree.insert('', 'end', 'parent', text='Parent')
tree.insert('parent', 'end', text='Child 1')
tree.insert('parent', 'end', text='Child 2')
```

---

## 📚 Full Example

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
tree = ttk.Treeview(root, columns=('Name', 'Age'), show='headings')
tree.heading('Name', text='Name')
tree.heading('Age', text='Age')

tree.insert('', 'end', values=('Alice', 30))
tree.insert('', 'end', values=('Bob', 25))

tree.pack()
root.mainloop()
```

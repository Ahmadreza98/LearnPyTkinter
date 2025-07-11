## 📚 `ttk.Notebook`: Tabs in Tkinter

In Tkinter, **tabs** are created using the `ttk.Notebook` widget. Each tab is like a page that holds its own content (a Frame or widget group).

---

## 🧱 Basic Structure

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

notebook.add(tab1, text='Tab One')
notebook.add(tab2, text='Tab Two')

ttk.Label(tab1, text="This is Tab 1").pack()
ttk.Label(tab2, text="This is Tab 2").pack()

root.mainloop()
```

✅ This creates two tabs with labels inside each.

---



## 🛠 `ttk.Notebook` Parameters


| Parameter   | Description                  |
| ----------- | ---------------------------- |
| `height`  | Fixed height of the notebook |
| `width`   | Fixed width of the notebook  |
| `padding` | Padding around tabs          |
| `style`   | Custom ttk style             |

---

## 📥 Adding and Inserting Tabs

```python
notebook.add(frame, text="New Tab", padding=10)

# Insert at position 0
notebook.insert(0, frame, text="First Tab")
```

---

## 🧾 Managing Tabs

```python
notebook.tab(0, text="Updated Tab Name")  # Update label
notebook.forget(1)                        # Remove tab at index 1
notebook.index("current")                # Get index of current tab
```

---

## 🕹 Detecting Tab Changes

You can bind to the `<<NotebookTabChanged>>` event to react to tab switches.

```python
def on_tab_change(event):
    selected_tab = event.widget.select()
    tab_index = event.widget.index(selected_tab)
    print(f"Tab changed to index: {tab_index}")

notebook.bind("<<NotebookTabChanged>>", on_tab_change)
```

---

## 📑 Getting Tab Info

```python
tab_id = notebook.select()           # Get selected tab ID
tab_index = notebook.index(tab_id)   # Get index of selected tab
tab_text = notebook.tab(tab_id, "text")  # Get tab label
```

---

## 🎨 Customizing with Styles

You can customize the appearance of tabs using the `ttk.Style` system.

```python
style = ttk.Style()
style.configure("TNotebook.Tab", padding=[10, 5], font=('Arial', 10, 'bold'))
```

You can also target individual tabs using tab IDs and the `style=` parameter when adding the tab.

---

## 🧭 Layout Tips

Each tab's content should be a `Frame` or any container widget.

For better structure:

```python
tab = ttk.Frame(notebook)
ttk.Label(tab, text="Content").grid(row=0, column=0)
ttk.Button(tab, text="Click").grid(row=1, column=0)
```

Use `grid()` or `pack()` inside the frame assigned to the tab.

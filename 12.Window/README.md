## 🪟 1. Main Window: `Tk()`

The **main application window** is created using `tk.Tk()`.

```python
import tkinter as tk

root = tk.Tk()
root.mainloop()
```

This is the **primary window** — only one `Tk()` instance should exist in a program.

---

## 🗂️ 2. Additional Windows: `Toplevel`

To open  **secondary windows** , use `tk.Toplevel`.

```python
def open_window():
    window = tk.Toplevel(root)
    window.title("New Window")
    tk.Label(window, text="This is a new window").pack()

button = tk.Button(root, text="Open Window", command=open_window)
button.pack()
```

* You can have multiple `Toplevel()` windows.
* Each acts as a separate popup or sub-window.

---

## ⚙️ 3. Window Properties

### ✅ Title

```python
root.title("My App")
```

### ✅ Size (geometry)

```python
root.geometry("600x400")  # width x height
```

### ✅ Min/Max Size

```python
root.minsize(300, 200)
root.maxsize(800, 600)
```

### ✅ Make Window Not Resizable

```python
root.resizable(False, False)  # width, height
```

---

## 🖼️ 4. Icon and Fullscreen

### Set Window Icon

```python
root.iconbitmap("my_icon.ico")  # Windows .ico file
```

For cross-platform apps, use PNG with `.iconphoto()`:

```python
icon = tk.PhotoImage(file='icon.png')
root.iconphoto(False, icon)
```

### Fullscreen

```python
root.attributes('-fullscreen', True)
```

Disable fullscreen:

```python
root.attributes('-fullscreen', False)
```

---

## 🪟 5. Window States

```python
root.state('zoomed')   # Maximized (Windows only)
root.state('iconic')   # Minimized
root.state('normal')   # Restored
```

---

## 💬 6. Dialogs (Popups)

Use the `tkinter.messagebox` module for alerts:

```python
from tkinter import messagebox

messagebox.showinfo("Title", "Information Message")
messagebox.showwarning("Warning", "This is a warning")
messagebox.showerror("Error", "Something went wrong")
```

And the `filedialog` module for file selection:

```python
from tkinter import filedialog

filename = filedialog.askopenfilename()
```

---

## 🧪 7. Detecting Close Events

Use the `"WM_DELETE_WINDOW"` protocol to control window close behavior:

```python
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
```

---

## 🧭 8. Focus and Window Order

### Bring window to front

```python
root.lift()
```

### Set window focus

```python
root.focus_force()
```

---

## 🧼 Summary


| Task            | Method                                     |
| --------------- | ------------------------------------------ |
| Main window     | `tk.Tk()`                                |
| New window      | `tk.Toplevel()`                          |
| Title           | `.title("App")`                          |
| Size            | `.geometry("600x400")`                   |
| Resizable       | `.resizable(False, False)`               |
| Position        | `.geometry("600x400+100+50")`            |
| Fullscreen      | `.attributes('-fullscreen', True)`       |
| Icon            | `.iconbitmap()`/`.iconphoto()`         |
| Closing handler | `.protocol("WM_DELETE_WINDOW", handler)` |
| Message boxes   | `messagebox.showinfo()`etc.              |
| File dialog     | `filedialog.askopenfilename()`           |

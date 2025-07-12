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

---

## 🧱 `window.attributes()` in Tkinter

The `.attributes()` method is used to  **get or set advanced properties of a window** , such as:

| Attribute             | Description                                               |
| --------------------- | --------------------------------------------------------- |
| `-fullscreen`       | Makes window fill the entire screen                       |
| `-topmost`          | Keeps window always on top                                |
| `-alpha`            | Sets transparency (0.0 = fully transparent, 1.0 = opaque) |
| `-toolwindow`       | Hides from taskbar (Windows only)                         |
| `-disabled`         | Disables the window (Windows only)                        |
| `-transparentcolor` | Makes a specific color fully transparent (Windows only)   |

---

## 🔹 Syntax

```python
# Set attribute
root.attributes("-topmost", True)

# Get attribute value
is_topmost = root.attributes("-topmost")
```

---

## ✅ Fullscreen Mode

```python
root.attributes("-fullscreen", True)
```

* Escape fullscreen:

```python
root.attributes("-fullscreen", False)
```

🔁 You can toggle it using a keyboard event:

```python
def toggle_fullscreen(event=None):
    current = root.attributes("-fullscreen")
    root.attributes("-fullscreen", not current)

root.bind("<F11>", toggle_fullscreen)
```

---

## ✅ Always-On-Top Window

```python
root.attributes("-topmost", True)   # Window always stays above others
```

---

## ✅ Window Transparency (`-alpha`)

Set window opacity between `0.0` (fully transparent) and `1.0` (fully opaque):

```python
root.attributes("-alpha", 0.7)
```

💡 Great for splash screens or overlays.

---

## ✅ Hide from Taskbar (Windows Only)

```python
root.attributes("-toolwindow", True)
```

* Makes the window borderless and removes it from taskbar.
* Often used for popup-like windows.

---

## ✅ Disable the Window (Windows Only)

```python
root.attributes("-disabled", True)
```

* The window becomes unclickable and unresponsive.
* Enable again with:

```python
root.attributes("-disabled", False)
```

---

## ✅ Transparent Background Color (Windows Only)

This makes a **specific color** transparent:

```python
root.configure(bg="pink")
root.attributes("-transparentcolor", "pink")
```

💡 Useful for overlay effects or shaped windows.

---

## 🧪 Full Example

```python
import tkinter as tk

root = tk.Tk()
root.geometry("400x200")
root.title("Window Attributes")

# Set attributes
root.attributes("-topmost", True)
root.attributes("-alpha", 0.85)
root.attributes("-fullscreen", False)

# Label
label = tk.Label(root, text="This window is semi-transparent and always on top.", font=("Arial", 12))
label.pack(pady=50)

root.mainloop()
```

---

## 🧼 Summary Table

| Attribute             | Platform | Description                        |
| --------------------- | -------- | ---------------------------------- |
| `-fullscreen`       | All      | Fills screen                       |
| `-topmost`          | All      | Keeps window above others          |
| `-alpha`            | All      | Controls transparency              |
| `-toolwindow`       | Windows  | Hides from taskbar, compact border |
| `-disabled`         | Windows  | Disables interaction               |
| `-transparentcolor` | Windows  | Makes a specific color transparent |

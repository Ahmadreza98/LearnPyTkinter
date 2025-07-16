# Tkinter `ttk.Frame` Widget

The `ttk.Frame` widget in Tkinter is a **container** used to group and organize other widgets. It's part of the `ttk` (themed Tkinter) module and provides a modern appearance.

---

## 🧱 Creating a Frame with `ttk`

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
frame = ttk.Frame(root, padding=10)
frame.pack()
```

- `padding=10`: Adds internal padding inside the frame.
- The frame must be packed, gridded, or placed into the layout.

---

## ⚙️ Frame Options


| Option      | Description                           |
| ----------- | ------------------------------------- |
| `padding` | Adds space inside the frame           |
| `width`   | Frame width (optional)                |
| `height`  | Frame height (optional)               |
| `style`   | Applies a custom ttk style (optional) |

> Note: `ttk.Frame` does not support border styles (`relief`, `borderwidth`). Use `tk.Frame` if you need those.



---



## 📦 Adding Widgets to a Frame

```python
label = ttk.Label(frame, text="Inside the frame")
label.pack()

```

- You can add any other widget inside the frame and manage their layout independently.

---



## 📐 Example with Multiple Frames

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

top_frame = ttk.Frame(root, padding=5)
top_frame.pack(side="top", fill="x")

bottom_frame = ttk.Frame(root, padding=5)
bottom_frame.pack(side="bottom", fill="x")

ttk.Label(top_frame, text="Top Area").pack()
ttk.Button(bottom_frame, text="OK").pack()

root.mainloop()

```

---

## 🎛 Frames with `grid()`

Frames are useful with `grid()` to keep widgets grouped:

```python
frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0)

ttk.Label(frame, text="Username:").grid(row=0, column=0)
ttk.Entry(frame).grid(row=0, column=1)

```

---

## 🔳 Frame vs LabelFrame


| Widget             | Purpose                       |
| ------------------ | ----------------------------- |
| `ttk.Frame`      | Basic container               |
| `ttk.LabelFrame` | Frame with a title and border |

Example:

```python
labelframe = ttk.LabelFrame(root, text="User Info", padding=10)
labelframe.pack()

```

---

## ✅ When to Use `ttk.Frame`

* To group related widgets
* For modular UI design
* As a layout organizer with `pack`, `grid`, or `place`

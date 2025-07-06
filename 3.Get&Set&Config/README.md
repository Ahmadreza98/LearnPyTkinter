# Tkinter `ttk` Widgets: `.get()`, `.set()`, and `.config()`

When working with Tkinter and `ttk` widgets, understanding how to retrieve and update widget data or properties is essential. This guide explains the use of `.get()`, `.set()`, and `.config()`.

---

## 📥 `.get()` – Retrieve Widget Values

Used to **get the current value** from widgets like `Entry`, `Combobox`, `Text`, etc.

### ✅ Examples

#### Entry

```python
name = entry.get()
```

#### Combobox

```python
selected_option = combobox.get()
```

#### Checkbutton / Radiobutton

```python
choice = variable.get()
```

> Note: You get the value from the **associated variable**, not directly from the widget.

---

## 📝 `.set()` – Set Widget Values

Used to **set a new value** to widgets. Typically used with control variables (like `StringVar`, `IntVar`, etc.)

### ✅ Examples

#### Set Entry or Combobox value using variable

```python
var = tk.StringVar()
entry = ttk.Entry(root, textvariable=var)
var.set("John Doe")  # Sets the entry value
```

#### Set Checkbutton / Radiobutton

```python
var = tk.BooleanVar()
check = ttk.Checkbutton(root, variable=var)
var.set(True)  # Checks the box
```

---

## ⚙️ `.config()` or `.configure()` – Change Widget Properties

Used to update the appearance or behavior of widgets **after creation**.

### ✅ Examples

#### Change Label text

```python
label.config(text="Updated!")
```

#### Change Button state

```python
button.config(state="disabled")
```

#### Update Progressbar value

```python
progress.config(value=70)
```

---

## 🔁 Summary Table

| Method        | Purpose                  | Usage Example                     |
| ------------- | ------------------------ | --------------------------------- |
| `.get()`    | Retrieve widget value    | `entry.get()`                   |
| `.set()`    | Set value (via variable) | `var.set("Hello")`              |
| `.config()` | Change widget property   | `label.config(text="New Text")` |

---

## 💡 Tip:

- Use `StringVar`, `IntVar`, `BooleanVar` to link values between the widget and your program logic.
- `config()` and `configure()` are the same; use whichever you prefer.

---

## 🔚 Conclusion

Understanding `.get()`, `.set()`, and `.config()` is key to interacting with user input and controlling your GUI dynamically in Tkinter with `ttk`. Mastering these will allow you to build powerful and responsive desktop apps!

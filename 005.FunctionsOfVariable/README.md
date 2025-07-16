# Tkinter `ttk` Widgets: Using `command` with Functions and Arguments

In Tkinter, many `ttk` widgets (like `Button`, `Checkbutton`, and `Radiobutton`) support the `command` option. This lets you assign a function that runs when the widget is interacted with (e.g., clicked).

---

## 🔘 Basic `command` Usage

You can assign a function to `command`:

```python
def say_hello():
    print("Hello!")

button = ttk.Button(root, text="Greet", command=say_hello)
```

---

## 🧩 Passing Arguments to `command`

You **cannot directly** pass arguments in `command=func(args)` because the function will be executed immediately. Instead, use `lambda` or `functools.partial`.

---

## ✅ Method 1: Using `lambda`

```python
def greet(name):
    print(f"Hello, {name}!")

button = ttk.Button(root, text="Greet John", command=lambda: greet("John"))
```

### Example with multiple arguments:

```python
def add(a, b):
    print(a + b)

btn = ttk.Button(root, text="Add", command=lambda: add(3, 5))
```

---

## ✅ Method 2: Using `functools.partial`

```python
from functools import partial

def greet(name):
    print(f"Hello, {name}!")

greet_john = partial(greet, "John")
button = ttk.Button(root, text="Greet John", command=greet_john)
```

---

## 🔁 Common Widgets with `command`

| Widget              | Purpose                               |
| ------------------- | ------------------------------------- |
| `ttk.Button`      | Perform an action on click            |
| `ttk.Checkbutton` | Toggle state and call function        |
| `ttk.Radiobutton` | Select option and call function       |
| `ttk.Scale`       | Can use `command` to track movement |

---

## 🎛 Example: Radiobutton with Arguments

```python
def choose(option):
    print(f"You chose: {option}")

ttk.Radiobutton(root, text="Option A", command=lambda: choose("A")).pack()
ttk.Radiobutton(root, text="Option B", command=lambda: choose("B")).pack()
```

---

## ⚠️ Things to Watch Out For

- Do **not** write `command=my_func()` — this will run the function immediately.
- Use `lambda:` or `partial()` to delay execution until the widget is interacted with.

---

## 🧪 Bonus: Update UI Using Commands

```python
def update_label():
    label.config(text="Updated!")

label = ttk.Label(root, text="Original")
button = ttk.Button(root, text="Update", command=update_label)
```

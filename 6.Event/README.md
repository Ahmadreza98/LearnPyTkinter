# Tkinter `ttk` Widgets: Event Handling

In Tkinter, you can make your GUI interactive by responding to **events** like key presses, mouse clicks, focus changes, etc. This is done using the `.bind()` method, which attaches event listeners to widgets.

---

## 🔄 What is an Event?

An **event** is an action performed by the user or the system, such as:

- Keyboard key press
- Mouse movement or click
- Widget gaining/losing focus
- Window resizing

---

## 🧩 Syntax: `.bind(event, handler)`

```python
widget.bind("<EventName>", handler_function)
```

The `handler_function` must accept at least one parameter (usually named `event`).

---

## 🖱 Common Events and Their Names

| Event Description   | Event Name                                                         |
| ------------------- | ------------------------------------------------------------------ |
| Key press           | `<Key>`                                                          |
| Specific key press  | `<Return>` (Enter), `<Escape>`, `<Up>`, etc.                 |
| Mouse click (left)  | `<Button-1>`                                                     |
| Mouse click (right) | `<Button-3>`                                                     |
| Double-click        | `<Double-Button-1>`                                              |
| Mouse enter/leave   | `<Enter>`, `<Leave>`                                           |
| Focus in/out        | `<FocusIn>`, `<FocusOut>`                                      |
| Mouse wheel scroll  | `<MouseWheel>` (Windows) / `<Button-4>`/`<Button-5>` (Linux) |

---

## ✅ Example: Key Press Event

```python
def on_key(event):
    print("You pressed:", event.char)

entry = ttk.Entry(root)
entry.pack()
entry.bind("<Key>", on_key)
```

---

## ✅ Example: Mouse Click on Button

```python
def on_click(event):
    print("Button clicked!")

button = ttk.Button(root, text="Click Me")
button.pack()
button.bind("<Button-1>", on_click)
```

---

## ✅ Example: Hover Effect

```python
def on_enter(event):
    event.widget.config(style="Hover.TButton")

def on_leave(event):
    event.widget.config(style="TButton")

button = ttk.Button(root, text="Hover me")
button.pack()
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)
```

---

## 🔀 Multiple Events on One Widget

You can bind multiple events to a single widget:

```python
entry.bind("<FocusIn>", lambda e: print("Got focus"))
entry.bind("<FocusOut>", lambda e: print("Lost focus"))
```

---

## 📦 Accessing Event Information

The `event` object contains useful info:

- `event.widget` → The widget that triggered the event
- `event.x`, `event.y` → Mouse position (for mouse events)
- `event.char`, `event.keysym` → Key press details

---

## 🧪 Universal Binding (to All Widgets)

You can bind events globally using `root.bind_all`:

```python
root.bind_all("<Escape>", lambda e: root.quit())
```

---

## 🧰 Summary

- Use `.bind()` to attach custom behavior to events.
- Make your apps more dynamic and interactive with event-driven design.
- You can also use `.unbind()` to remove an event handler.

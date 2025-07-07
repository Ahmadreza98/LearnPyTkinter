# Tkinter Canvas Widget

The `Canvas` widget in Tkinter is a powerful tool for creating drawings, animations, and custom widgets. It allows you to draw shapes, place images, and create complex graphical interfaces.

---

## 📐 What Is Canvas?

`Canvas` provides a space where you can draw:

- Lines
- Rectangles
- Ovals and circles
- Polygons
- Arcs
- Text
- Images
- Widgets (indirectly)

---

## 🧱 Creating a Canvas

```python
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack()
```

---

## ✏️ Drawing Shapes

### Line

```python
canvas.create_line(x1, y1, x2, y2, **options)
```

Example:

```python
canvas.create_line(10, 10, 200, 50, fill="blue", width=2)
```

### Rectangle

```python
canvas.create_rectangle(x1, y1, x2, y2, **options)
```

### Oval (including circles)

```python
canvas.create_oval(x1, y1, x2, y2, **options)
```

### Polygon

```python
canvas.create_polygon(x1, y1, x2, y2, x3, y3, ..., **options)
```

### Arc

```python
canvas.create_arc(x1, y1, x2, y2, start=0, extent=90, **options)
```

---

## 🔤 Adding Text

```python
canvas.create_text(x, y, text="Hello Canvas", font=("Arial", 14), fill="black")
```

---

## 🖼 Adding Images

```python
from tkinter import PhotoImage

img = PhotoImage(file="path/to/image.png")
canvas.create_image(x, y, image=img, anchor="nw")
```

> Note: Keep a reference to `img` to prevent garbage collection.

---

## 🧭 Canvas Options

| Option           | Description             |
| ---------------- | ----------------------- |
| `bg`           | Background color        |
| `width`        | Width of canvas         |
| `height`       | Height of canvas        |
| `scrollregion` | Defines scrollable area |

---

## 🧹 Deleting or Updating Items

Canvas items return an ID you can use to update or delete them:

```python
line_id = canvas.create_line(0, 0, 100, 100)
canvas.delete(line_id)
canvas.itemconfig(line_id, fill="red")
```

---

## 🔍 Canvas Events

Canvas supports event bindings like other widgets:

```python
canvas.bind("<Button-1>", callback)
```

You can get click coordinates via `event.x`, `event.y`.

---

## 📜 Scrollable Canvas Example

```python
scroll = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.config(yscrollcommand=scroll.set)
scroll.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
```

---

## 🧮 Coordinate System

- (0, 0) is the top-left corner
- All drawing is based on absolute positions
- Use `canvas.move(item, dx, dy)` to shift items

---

## 🔚 Summary

The `Canvas` widget is ideal for custom graphics, complex layouts, and game development. It offers:

- Flexible drawing
- Event support
- Dynamic updates
- Scrollable areas

Canvas is one of the most versatile widgets in Tkinter!

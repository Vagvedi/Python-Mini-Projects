import tkinter as tk
from tkinter import colorchooser

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Paint App")
        self.root.geometry("800x500")
        self.root.resizable(False, False)

        self.current_color = "black"

        top_bar = tk.Frame(root)
        top_bar.pack(fill="x")

        tk.Button(top_bar, text="Color", width=10, command=self.choose_color).pack(side="left", padx=5)
        tk.Button(top_bar, text="Clear", width=10, command=self.clear_canvas).pack(side="left", padx=5)

        self.canvas = tk.Canvas(root, bg="white", width=780, height=440)
        self.canvas.pack(pady=10)

        self.canvas.bind("<B1-Motion>", self.paint)

    def paint(self, event):
        x1, y1 = (event.x - 2), (event.y - 2)
        x2, y2 = (event.x + 2), (event.y + 2)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.current_color, outline=self.current_color)

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.current_color = color

    def clear_canvas(self):
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    PaintApp(root)
    root.mainloop()

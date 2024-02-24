import tkinter as tk

class DrawingPad:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing Pad")

        self.canvas = tk.Canvas(root, bg="white", width=500, height=500)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.old_x = None
        self.old_y = None

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

    def paint(self, event):
        x, y = event.x, event.y
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, x, y, width=2, fill="black", capstyle=tk.ROUND, smooth=tk.TRUE)

        self.old_x = x
        self.old_y = y

    def reset(self, event):
        self.old_x = None
        self.old_y = None

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingPad(root)
    root.mainloop()

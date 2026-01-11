import tkinter as tk
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.root.resizable(False, False)

        self.running = False
        self.start_time = 0
        self.elapsed = 0

        self.time_label = tk.Label(
            root, text="00:00:00.00",
            font=("Arial", 36, "bold"),
            padx=20, pady=20
        )
        self.time_label.pack()

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Start", width=10, command=self.start).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Stop", width=10, command=self.stop).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Reset", width=10, command=self.reset).grid(row=0, column=2, padx=5)

        self.update_display()

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed

    def stop(self):
        if self.running:
            self.running = False
            self.elapsed = time.time() - self.start_time

    def reset(self):
        self.running = False
        self.start_time = 0
        self.elapsed = 0
        self.time_label.config(text="00:00:00.00")

    def update_display(self):
        if self.running:
            self.elapsed = time.time() - self.start_time

        hours = int(self.elapsed // 3600)
        minutes = int((self.elapsed % 3600) // 60)
        seconds = int(self.elapsed % 60)
        milliseconds = int((self.elapsed - int(self.elapsed)) * 100)

        self.time_label.config(
            text=f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:02d}"
        )
        self.root.after(10, self.update_display)

if __name__ == "__main__":
    root = tk.Tk()
    Stopwatch(root)
    root.mainloop()

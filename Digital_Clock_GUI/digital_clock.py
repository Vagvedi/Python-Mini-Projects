import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime("%H:%M:%S %p")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock")
root.geometry("350x150")
root.resizable(False, False)

clock_label = tk.Label(
    root,
    font=("Arial", 40, "bold"),
    bg="black",
    fg="cyan",
    pady=20
)
clock_label.pack(fill="both", expand=True)

update_time()
root.mainloop()

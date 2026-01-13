import tkinter as tk
from tkinter import messagebox, filedialog

def new_note():
    text_area.delete(1.0, tk.END)

def save_note():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))
        messagebox.showinfo("Saved", "Note saved successfully")

def open_note():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, content)

root = tk.Tk()
root.title("Notes App")
root.geometry("500x500")
root.resizable(False, False)

title = tk.Label(root, text="🗒️ Notes App", font=("Arial", 18, "bold"))
title.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="New", width=10, command=new_note).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Open", width=10, command=open_note).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Save", width=10, command=save_note).grid(row=0, column=2, padx=5)

text_area = tk.Text(root, font=("Arial", 12), wrap="word")
text_area.pack(padx=10, pady=10, fill="both", expand=True)

root.mainloop()

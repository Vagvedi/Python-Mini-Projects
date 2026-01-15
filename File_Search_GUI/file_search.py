import tkinter as tk
from tkinter import filedialog, messagebox
import os

def browse_folder():
    folder = filedialog.askdirectory()
    folder_path.set(folder)

def search_file():
    filename = file_entry.get().strip()
    folder = folder_path.get()

    result_box.delete(1.0, tk.END)

    if not filename or not folder:
        messagebox.showwarning("Input Error", "Please provide file name and folder")
        return

    found = False
    for root, dirs, files in os.walk(folder):
        if filename in files:
            result_box.insert(tk.END, os.path.join(root, filename) + "\n")
            found = True

    if not found:
        result_box.insert(tk.END, "❌ File not found")

root = tk.Tk()
root.title("File Search Tool")
root.geometry("550x400")
root.resizable(False, False)

tk.Label(root, text="🔍 File Search Tool", font=("Arial", 18, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Label(frame, text="File Name:", font=("Arial", 12)).grid(row=0, column=0, padx=5, sticky="e")
file_entry = tk.Entry(frame, font=("Arial", 12), width=30)
file_entry.grid(row=0, column=1, padx=5)

tk.Label(frame, text="Folder:", font=("Arial", 12)).grid(row=1, column=0, padx=5, sticky="e")
folder_path = tk.StringVar()
folder_entry = tk.Entry(frame, textvariable=folder_path, font=("Arial", 12), width=30)
folder_entry.grid(row=1, column=1, padx=5)

tk.Button(frame, text="Browse", command=browse_folder).grid(row=1, column=2, padx=5)

tk.Button(root, text="Search", width=15, command=search_file).pack(pady=10)

result_box = tk.Text(root, font=("Arial", 11), height=10)
result_box.pack(padx=10, pady=10, fill="both", expand=True)

root.mainloop()

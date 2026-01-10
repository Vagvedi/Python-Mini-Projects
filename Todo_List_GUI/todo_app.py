import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    try:
        selected = task_listbox.curselection()
        task_listbox.delete(selected)
    except:
        pass

def mark_done():
    try:
        selected = task_listbox.curselection()[0]
        task = task_listbox.get(selected)
        task_listbox.delete(selected)
        task_listbox.insert(tk.END, f"✔ {task}")
    except:
        pass

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x450")
root.resizable(False, False)

title = tk.Label(root, text="📝 To-Do List", font=("Arial", 18, "bold"))
title.pack(pady=10)

task_entry = tk.Entry(root, font=("Arial", 14))
task_entry.pack(padx=20, pady=10, fill="x")

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

add_btn = tk.Button(btn_frame, text="Add Task", width=12, command=add_task)
add_btn.grid(row=0, column=0, padx=5)

done_btn = tk.Button(btn_frame, text="Mark Done", width=12, command=mark_done)
done_btn.grid(row=0, column=1, padx=5)

delete_btn = tk.Button(btn_frame, text="Delete Task", width=12, command=delete_task)
delete_btn.grid(row=0, column=2, padx=5)

task_listbox = tk.Listbox(
    root,
    font=("Arial", 14),
    height=12,
    selectbackground="lightblue"
)
task_listbox.pack(padx=20, pady=10, fill="both", expand=True)

root.mainloop()

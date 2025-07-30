import tkinter as tk
from tkinter import messagebox
import os

FILE_NAME = "todo.txt"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                task_list.insert(tk.END, line.strip())

def save_tasks():
    with open(FILE_NAME, "w") as file:
        tasks = task_list.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Saved", "Tasks saved to todo.txt")

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    selected = task_list.curselection()
    if selected:
        task_list.delete(selected)
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# GUI setup
root = tk.Tk()
root.title("📋 To-Do List App")
root.geometry("400x400")

frame = tk.Frame(root)
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=30, font=("Arial", 12))
task_entry.grid(row=0, column=0, padx=10)

add_btn = tk.Button(frame, text="Add Task", command=add_task)
add_btn.grid(row=0, column=1)

task_list = tk.Listbox(root, width=40, height=15, font=("Arial", 11))
task_list.pack(pady=10)

del_btn = tk.Button(root, text="Delete Selected", command=delete_task)
del_btn.pack()

save_btn = tk.Button(root, text="Save Tasks", command=save_tasks)
save_btn.pack(pady=5)

# Load saved tasks on startup
load_tasks()

root.mainloop()

import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("To-Do List")

# List to store tasks
tasks = []

# Function to add a task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Function to edit a task
def edit_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        new_task = task_entry.get()
        if new_task:
            tasks[selected_task_index] = new_task
            update_listbox()
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

# Function to delete a task
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        del tasks[selected_task_index]
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

# Function to update the task listbox
def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# GUI Components
task_entry = tk.Entry(root, font=("Arial", 14))
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

edit_button = tk.Button(root, text="Edit Task", command=edit_task)
edit_button.pack()

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

task_listbox = tk.Listbox(root, font=("Arial", 14), width=40, height=10)
task_listbox.pack(pady=10)

# Run the application
root.mainloop()

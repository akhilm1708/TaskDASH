import tkinter as tk
from tkinter import messagebox
from task_manager import *
from calendar_api import authenticate_google, add_task_to_calendar


def create_ui():
    tasks = load_tasks()

    def refresh_task_list():
        #listbox to view all tasks
        tasks_listbox.delete(0, tk.END)
        sorted_tasks = sort_tasks_by_priority(tasks)
        print(sorted_tasks)
        for task in sorted_tasks:
            #iterating to insert into listbox
            tasks_listbox.insert(tk.END,f"{task['title']} (Priority{task['priority']}) -Due: {task['due_date']}")

    def add_task():
        title = task_title_entry.get()
        priority = int(priority_entry.get())
        due_date = due_date_entry.get()
        if title and due_date:
            add_task_to_list(tasks, title, priority, due_date)
            add_task_to_calendar(title, due_date)
            refresh_task_list()
        else:
            messagebox.showwarning("Input Error", "Please provide all details.")

    def delete_task():
        # delete task w/ check for index
        try:
            selected_index = tasks_listbox.curselection()[0]
            delete_task_from_list(tasks, selected_index)
            refresh_task_list()  #refresh after deletion
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

        

    root = tk.Tk()
    root.title("To-Do List App")
    tk.Label(root, text="Task Title").pack()

    task_title_entry = tk.Entry(root)
    task_title_entry.pack()

    tk.Label(root, text="Priority (1 = High, 3 = Low)").pack()
    priority_entry = tk.Entry(root)
    priority_entry.pack()

    tk.Label(root, text="Due Date (YYYY-MM-DD)").pack()
    due_date_entry = tk.Entry(root)
    due_date_entry.pack()

    add_button = tk.Button(root, text="Add Task", command=add_task)
    add_button.pack()

    delete_button = tk.Button(root, text="Delete Task", command=delete_task)
    delete_button.pack()

    tasks_listbox = tk.Listbox(root, width=50, height=15)
    tasks_listbox.pack()

    refresh_task_list()
    root.mainloop()

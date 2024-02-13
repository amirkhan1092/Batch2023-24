import tkinter as tk

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        self.tasks = []

        self.task_entry = tk.Entry(master, width=40)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        self.task_listbox = tk.Listbox(master, width=50)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
    
        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=0, padx=5, pady=5)

        self.clear_button = tk.Button(master, text="Clear All", command=self.clear_tasks)
        self.clear_button.grid(row=2, column=1, padx=5, pady=5)

    def add_task(self):
        task_text = self.task_entry.get()
        if task_text:
            self.tasks.append(task_text)
            self.task_listbox.insert(tk.END, task_text)
            self.task_entry.delete(0, tk.END)
    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
            del self.tasks[selected_index]
        except IndexError:
            pass
    def clear_tasks(self):
        self.tasks = []
        self.task_listbox.delete(0, tk.END)




if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

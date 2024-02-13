# To Do List
import tkinter as tk

class ToDo:
    def __init__(self, win) -> None:
        self.win = win
        win.title('To Do List')
        win.geometry('400x300')

        self.entry = tk.Entry(win)
        self.entry.grid(row=0, column=0)
        tk.Button(win, text='Add Item', command=self.add_item).grid(row=0, column=1)

        self.list_box = tk.Listbox(win, width=40)
        self.list_box.grid(row=1, column=0, columnspan=2)

        tk.Button(win, text='Delete Item', command=self.delete_item).grid(row=2, column=0)
        tk.Button(win, text='Delete All', command=self.clear_list).grid(row=2, column=1)

    def add_item(self):
        data = self.entry.get()
        self.list_box.insert(tk.END, data)
        self.entry.delete(0, tk.END)
    def delete_item(self):
        sel_index = self.list_box.curselection()
        self.list_box.delete(sel_index)
    def clear_list(self):
        self.list_box.delete(0, tk.END)





# main
root = tk.Tk()
app = ToDo(root)
root.mainloop()
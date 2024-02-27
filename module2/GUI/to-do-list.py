# To Do List

import tkinter as tk


class ToDoList:
    def __init__(self, win) -> None:
        self.win = win
        win.title('To-Do-List')

        self.entry = tk.Entry(win, width=20)
        self.entry.grid(row=0, column=0)
        
        self.bt1 = tk.Button(win, text='Add Item', command=self.addItem)
        self.bt1.grid(row=0, column=1)

        self.listbox = tk.Listbox(win, width=40)
        self.listbox.grid(row=1, column=0, columnspan=2)

        self.bt2 = tk.Button(win, text='Delete Item', command=self.delItem)
        self.bt2.grid(row=2, column=0)

        self.bt3 = tk.Button(win, text='Delete All Item', command=self.delallItem)
        self.bt3.grid(row=2, column=1)
        
    def addItem(self):
        data = self.entry.get()
        self.entry.delete(0, tk.END)
        self.listbox.insert(tk.END, data)
    def delItem(self):
        index = self.listbox.curselection()
        self.listbox.delete(index)
    def delallItem(self):
        pass



# main code
root = tk.Tk()
exc = ToDoList(root)
root.mainloop()
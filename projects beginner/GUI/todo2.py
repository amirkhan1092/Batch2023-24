import tkinter as tk

# To Do List
class to_do_list:
    def __init__(self,mainwindow) -> None:
        self.mainwindow = mainwindow
        
        self.en1 = tk.Entry(mainwindow)
        self.en1.grid(row=0, column=0)

        self.bt1 = tk.Button(mainwindow,text='Add Item', command=self.add_item)
        self.bt1.grid(row=0, column=1)

        self.list_box = tk.Listbox(width=30)
        self.list_box.grid(row=1, column=0, columnspan=2)

        self.bt2 = tk.Button(mainwindow,text='Delete Item', command=self.del_item)
        self.bt2.grid(row=2, column=0)

        self.bt3 = tk.Button(mainwindow, text='Delete All Items', command=self.del_all_item)
        self.bt3.grid(row=2, column=1)

    def add_item(self):
        data = self.en1.get()
        self.list_box.insert(tk.END, data)
    
    def del_item(self):
        self.list_box.delete(self.list_box.curselection())
    
    def del_all_item(self):
        self.list_box.delete(0, tk.END)

root = tk.Tk()
to_do_list(root)
root.mainloop()
from tkinter import *
class to_do:
    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        self.mainwindow.geometry("500x500")
        self.mainwindow.title("To Do List")
        self.lb = Label(self.mainwindow, text = "Enter :-")
        self.lb.grid(row = 0, column = 0)
        self.e = Entry(self.mainwindow)
        self.e.grid(row = 1, column = 0)
        self.b = Button(self.mainwindow, text = "ADD", command = self.add_item)
        self.b.grid(row = 1, column = 1)
        self.list_box = Listbox(self.mainwindow)
        self.list_box.grid(row = 2, column = 0)
        self.b_del_1 = Button(self.mainwindow, text = "Delete This Item", command = self.delete_item)
        self.b_del_1.grid(row = 3, column = 0)
        self.b_del_all = Button(self.mainwindow, text = "Delete All Items", command = self.delete_items)
        self.b_del_all.grid(row = 3, column = 1)

        self.undo = Button(self.mainwindow, text = "Undo", command = self.undo_itm)
        self.undo.grid()
        self.list = []
    def add_item(self):
        item = self.e.get()
        self.list_box.insert(END, item)
        self.e.delete(0, END)
    def delete_item(self):
        index = self.list_box.curselection()
        val = self.list_box.get(index)
        self.list.append([index, val])
        self.list_box.delete(index)
    def delete_items(self):
        self.list_box.delete(0, END)

    def undo_itm(self):
        if self.list:
            index, val = self.list.pop()
            self.list_box.insert(index, val)
root = Tk()
exe = to_do(root)
root.mainloop()
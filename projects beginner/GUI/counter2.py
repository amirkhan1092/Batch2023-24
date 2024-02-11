# basic counter 
from tkinter import *
class Counter:
    def __init__(self, mainwindow) -> None:
        self.mainwindow = mainwindow

        mainwindow.geometry("300x200")
        mainwindow.title("Counter App")
        mainwindow.maxsize(500,500)
        mainwindow.minsize(100,100)
        # global initialization 
        self.var = IntVar(value=0)
        self.lb = Label(root,textvariable=self.var, font=('bold', 30), fg = 'green')
        self.lb.pack()
        self.bt1 = Button(root,text = "Increment",command = self.increment)
        self.bt1.pack(side=LEFT, ipadx=10, ipady=10, padx=10, pady=10)
        self.bt2 = Button(root,text = "decrement",command = self.decrement)
        self.bt2.pack(side=RIGHT, ipadx=10, ipady=10, padx=10, pady=10)   

    def increment(self):
        data = self.var.get() + 1
        self.var.set(data)
        if data >= 10:
            self.lb.config(fg='red')
        else:
            self.lb.config(fg='green')   
    def decrement(self):
        data = self.var.get() - 1
        if data >= 0:
            self.var.set(data)
        if data >= 10:
            self.lb.config(fg='red')
        else:
            self.lb.config(fg='green') 

# main window 
root = Tk()
exe = Counter(root)
root.mainloop()





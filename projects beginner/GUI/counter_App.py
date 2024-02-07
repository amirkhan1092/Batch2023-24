# import tkinter 
import tkinter as tk

class counterApp:
    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        mainwindow.geometry('200x100')
        mainwindow.title('Counter App')

        self.var = tk.IntVar(value=0)
        # add widgets
        self.lbl1 = tk.Label(mainwindow,textvariable=self.var, font=('BOLD', 30))
        self.lbl1.pack()

        self.btn1 = tk.Button(mainwindow,text="Increment",command=self.increment)
        self.btn1.pack(side=tk.LEFT)
        self.btn2 = tk.Button(mainwindow,text="Decrement",command=self.decrement)
        self.btn2.pack(side=tk.RIGHT)

    # actions 
    def increment(self):
        data = self.var.get()+1
        self.var.set(data)
        if data >= 10:
            self.lbl1.config(fg='red')
        else:
            self.lbl1.config(fg='green')
    def decrement(self):
        data = self.var.get()-1
        if data < 0:
            pass
        else:
            self.var.set(data)
        if data >= 10:
            self.lbl1.config(fg='red')
        else:
            self.lbl1.config(fg='green')

# main code 
root = tk.Tk()
exc = counterApp(root)
root.mainloop()
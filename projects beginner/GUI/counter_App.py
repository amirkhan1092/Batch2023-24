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

        self.btn1 = tk.Button(mainwindow,text="Increment",command= lambda:self.action(1))
        self.btn1.pack(side=tk.LEFT)
        self.btn2 = tk.Button(mainwindow,text="Decrement",command=lambda:self.action(2))
        self.btn2.pack(side=tk.RIGHT)

    # actions 
    def action(self, a):
        data = self.var.get()
        if a == 1:
            self.var.set(data + 1)
        elif a == 2:
            self.val.set(data-1)


# main code 
root = tk.Tk()
exc = counterApp(root)
root.mainloop()
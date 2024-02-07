import tkinter as tk
class Counter:
    def __init__(self, mainwiondow):
        self.mainwiondow = mainwiondow
        mainwiondow.geometry('300x200')
        mainwiondow.title('Counter App')
        mainwiondow.minsize(200, 100)
        mainwiondow.maxsize(300, 200)
        self.var = tk.IntVar(value=0)
        tk.Label(mainwiondow, text='Welcome to Counter App').pack()
        lab1 = tk.Label(mainwiondow, textvariable=self.var, font=('bold', 24))
        lab1.pack()

        bt1 = tk.Button(mainwiondow, text='Increment', command=self.action1)
        bt1.pack(side=tk.LEFT, ipadx=10, ipady=10)

        bt2 = tk.Button(mainwiondow, text='Decrement', command=self.action2)
        bt2.pack(side=tk.RIGHT, ipadx=10, ipady=10)
        
    def action1(self):
        self.var.set(self.var.get() + 1)   
    def action2(self):   
        self.var.set(self.var.get() - 1)
# main code 
root = tk.Tk()
exe = Counter(root)
root.mainloop()

# Greeting App
import tkinter as tk

class app:
    def __init__(self, mainwindow):
        self.mainwindow = mainwindow

        tk.Label(mainwindow, text='Enter the Number').pack()
        
        self.name = tk.Entry(mainwindow)
        self.name.pack()
        
        tk.Button(mainwindow, text='Enter', command=self.action).pack()
        self.out=tk.Label(mainwindow,text='')
        self.out.pack()
        

    def action(self):
        data = int(self.name.get())
        st = 'Not a Prime Number'
        count = 0
        for i in range(1, data+1):
            if data % i == 0:
                count += 1
        if count == 2:
            st = 'Prime Number'

        self.out.config(text=st)
        self.name.delete(0, tk.END)
    

# main loop
root = tk.Tk()
exe = app(root)
root.mainloop()
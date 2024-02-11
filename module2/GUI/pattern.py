# Greeting App
import tkinter as tk

class app:
    def __init__(self, mainwindow):
        self.mainwindow = mainwindow

        tk.Label(mainwindow, text='Enter the Number').pack()
        
        self.name = tk.Entry(mainwindow)
        self.name.pack()
        
        tk.Button(mainwindow, text='Enter', command=self.action).pack()
        self.out=tk.Label(mainwindow,text='', justify='left')
        self.out.pack()
        

    def action(self):
        data = int(self.name.get())
        s =''
        for i in range(1,data+1):
            st=''
            st = '* '*i
            s = s+st+'\n'
        self.out.config(text=s)
        self.name.delete(0, tk.END)
    

# main loop
root = tk.Tk()
exe = app(root)
root.mainloop()
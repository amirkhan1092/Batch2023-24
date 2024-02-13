# BMI Calculator

import tkinter as tk
class bmi:
    def __init__(self, win):
        self.win = win 
        win.geometry('400x300')
        win.title('BMI Calc')
        tk.Label(root, text="weight").grid(row=0, column=0)
        tk.Label(root, text="height" ).grid(row=1, column=0)
        self.w=tk.Entry(root)
        self.w.grid(row=0,column=1)
        self.h=tk.Entry(root)
        self.h.grid(row=1,column=1)
        b=tk.Button(root, text="click", command= self.click)
        b.grid(row=2, column=1)
        self.disp=tk.Label(root, text="")
        self.disp.grid(row=3, column=1)

    def click(self):
        n1=self.w.get()
        n2=self.h.get()
        m=int(n1)/int(n2)**2
        self.disp.config(text=m)




# main 
root = tk.Tk()
app = bmi(root)
root.mainloop()
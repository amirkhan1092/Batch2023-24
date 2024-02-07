# import tkinter as tk
from tkinter import *

root = Tk()
root.geometry('200x100')
root.title('First App')
root.minsize(100, 50)

def my_fun1():
    data = lb.cget('text')
    data += 1
    lb.config(text=data, bg='red')
def my_fun2():
    lb.config(text=lb.cget('text')-1)

lb = Label(root, text=0)
lb.pack()
bt1 = Button(root, text=' + ', command=my_fun1)
bt1.pack()
bt2 = Button(root, text=' - ', command=my_fun2)
bt2.pack()

root.mainloop()

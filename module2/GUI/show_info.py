import tkinter as tk
from tkinter import messagebox as mb


root = tk.Tk()
tk.Label(root, text='Enter the name').pack()

def action():
    mb.showinfo('Greet', 'hello,'+entry.get())
    


entry = tk.Entry(root)
entry.pack()

bt1 = tk.Button(root, text='Enter', command=action)
bt1.pack()


root.mainloop()



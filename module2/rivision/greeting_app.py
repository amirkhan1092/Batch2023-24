import tkinter as tk
from tkinter import messagebox as mb

# main window reference object
root = tk.Tk()
root.title("Greeting App")
root.geometry("400x300")
def action():
    disp.config(text='hello, '+ entry.get())
    entry.delete(0, tk.END)

tk.Label(root, text='Enter the name ').pack()

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text='Enter', command=action).pack()

disp = tk.Label(root, text='')
disp.pack()
root.mainloop()



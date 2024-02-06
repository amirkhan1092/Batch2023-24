from tkinter import *

root = Tk()
def exit_fun():
    root.destroy()

Label(root, text='Welcome to GUI App').pack()

Button(root, text='Exit', command=exit_fun).pack()

root.mainloop()
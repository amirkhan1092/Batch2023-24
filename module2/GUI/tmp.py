from tkinter import *
root = Tk()
def action():
    ltb.insert(0, 'hello')

ent = Entry(root)
ent.pack()

bt = Button(root, command=action)
bt.pack()

ltb = Listbox(root)
ltb.pack()

bt.mainloop()
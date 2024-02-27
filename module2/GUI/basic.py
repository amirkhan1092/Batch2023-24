import tkinter as tk

root = tk.Tk()
root.configure(bg='skyblue')
def action1():
    data = lb.cget('text')
    data = int(data) + 1
    lb.configure(text=str(data))
    print(txt.get(1.0, tk.END))
def action2():
    data = lb.cget('text')
    data = int(data) - 1
    lb.config(text=str(data))
lb = tk.Label(root, text='0', bg='red')
lb.pack()

txt = tk.Text(root)
txt.pack()
bt1 = tk.Button(root, text='  INC  ', command=action1)
bt1.pack()
bt2 = tk.Button(root, text='  DEC   ', command=action2)
bt2.pack()
root.mainloop()


import tkinter as tk
from tkinter import messagebox as mb


root = tk.Tk()
root.geometry('300x200')
root.title('Greeting App')
# root.config(bg='skyblue')

def action():
    count=0
    x=int(entry.get())
    for i in range(1,x):
        if x%i==0:
            count+=1
            if count>2:
                mb.showinfo('output','not a prime number')
            else:
                mb.showinfo('output','prime number')

    



msg = tk.Label(root, text='Enter the Number', font=('bold', 20))
msg.pack()
entry = tk.Entry(root)
entry.pack()

bt1 = tk.Button(root, text='Prime Check', command=action)
bt1.pack()

root.mainloop()
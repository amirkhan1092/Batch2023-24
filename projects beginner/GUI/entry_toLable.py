import tkinter as tk


root = tk.Tk()

def action():
    data = entry.get()
    count=0
    for i in range(1,int(data)+1):
        if int(data)%i==0:
            count+=1
    if count==2:
        disp.config(text="PRIME")
    else:
        disp.config(text="NOT PRIME")

    entry.delete(0, tk.END)


tk.Label(root, text='Enter the number').pack()

entry = tk.Entry(root)
entry.pack()

bt1 = tk.Button(root, text='prime check', command=action)
bt1.pack()

disp = tk.Label(root, text='')
disp.pack()
bt2 = tk.Button(root, text='Exit', command=root.destroy)
bt2.pack()

root.mainloop()
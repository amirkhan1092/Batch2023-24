# radio button 

'''
The Radiobutton is a standard Tkinter widget used to implement one-of-many selections. 
Radiobuttons can contain text or images, and you can associate a Python function or method with each button. 
When the button is pressed, Tkinter automatically calls that function or method.
Syntax: 
 

button = Radiobutton(master, text=”Name on Button”, variable = “shared variable”, 
value = “values of each button”, options = values, …)
shared variable = A Tkinter variable shared among all Radio buttons 
value = each radiobutton should have different value otherwise more than 1 radiobutton will get selected. 


'''

import tkinter as tk

root = tk.Tk()
root.geometry('400x400')
i = tk.IntVar(value=0)

tk.Label(root, text='The Right Option', anchor='w').place(x=0, y=10)
bt1 = tk.Radiobutton(root, text= 'option 1', value = 1, variable=i)
bt1.place(x=2, y=10)
bt2 = tk.Radiobutton(root, text= 'option 2', value = 2, variable=i)
bt2.place(x=4, y=10)

root.mainloop()
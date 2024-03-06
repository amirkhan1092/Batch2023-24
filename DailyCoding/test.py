import tkinter as tk 

def on_select(event): 

    selected_item = my_listbox.get(my_listbox.curselection()) 

    print(selected_item) 

root = tk.Tk() 

my_listbox = tk.Listbox(root) 

my_listbox.insert(1, "January") 

my_listbox.insert(2, "February") 

my_listbox.insert(3, "March") 

my_listbox.bind("<<ListboxSelect>>", on_select) 

my_listbox.pack() 

root.mainloop() 
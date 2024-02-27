import tkinter as tk
from tkinter import messagebox

class MessagePopUp:
    def __init__(self, win) -> None:
        self.win = win

        self.entry = tk.Entry(win)
        self.entry.pack()

        self.bt1 = tk.Button(win, text='Show Data',  command=self.action)
        self.bt1.pack()

    def action(self):
        # messagebox.showerror('Greeting', self.entry.get())
        var = messagebox.askquestion('Exit', 'Do you want to exit?')
        if var.casefold() == 'yes':
            self.win.destroy()

# main code
if __name__ == '__main__':
    root = tk.Tk()
    exc = MessagePopUp(root)
    root.mainloop()



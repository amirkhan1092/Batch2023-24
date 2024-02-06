'''
tkinter
wxpython
pyqt6
'''


from tkinter import *
class App:
    def __init__(self, mainwindow) -> None:
        self.mainwindow = mainwindow
        mainwindow.title('Counter App')
        mainwindow.geometry('400x200')
        mainwindow.minsize(200, 100) 
        self.var_text = IntVar(value=0)
        lb1 = Label(self.mainwindow, textvariable=self.var_text)
        lb1.pack()

        bt1 = Button(self.mainwindow, text=" +  ", command=self.action)
        bt2=Button(self.mainwindow,text="  -  ",command=self.action2)
        bt1.pack(side=LEFT, padx=20, pady=20, ipadx=50, ipady=20)
        bt2.pack(side=RIGHT, padx=20, pady=20, ipadx=50, ipady=20)

    def action(self):
        self.var_text.set(self.var_text.get()+1)

    def action2(self):
        self.var_text.set(self.var_text.get()-1)

# main code 
root = Tk()
exe = App(root)
root.mainloop()









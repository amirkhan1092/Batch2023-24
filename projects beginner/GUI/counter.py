# write the code here 
import tkinter as tk

class CounterApp:
    def __init__(self, master):
        self.master = master
        self.counter_value = tk.IntVar(value=0)
        
        self.label = tk.Label(master, textvariable=self.counter_value, font=('Arial', 24))
        self.label.pack(pady=20)

        self.increment_button = tk.Button(master, text="Increment", command=self.increment_counter)
        self.increment_button.pack(side=tk.LEFT, padx=10, ipadx=10, ipady=10)

        self.decrement_button = tk.Button(master, text="Decrement", command=self.decrement_counter)
        self.decrement_button.pack(side=tk.RIGHT, padx=10, ipadx=10, ipady=10)

    def increment_counter(self):
        self.counter_value.set(self.counter_value.get() + 1)

    def decrement_counter(self):
        if self.counter_value.get() > 0:
            self.counter_value.set(self.counter_value.get() - 1)

def main():
    root = tk.Tk()
    root.title("Counter App")
    app = CounterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import messagebox

def calculate_sum():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 + num2
        messagebox.showinfo("Result", f"The sum is: {result}")
    except ValueError:
        print(messagebox.showerror("Error", "Please enter valid numbers"))
        print(messagebox.showwarning("warnings", 'value exceeded'))
        print(messagebox.askquestion("warnings", 'value exceeded'))


# Create main application window
root = tk.Tk()
root.title("Sum Calculator")

# Create labels
label_num1 = tk.Label(root, text="Enter number 1:")
label_num1.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

label_num2 = tk.Label(root, text="Enter number 2:")
label_num2.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

# Create entry fields
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

# Create button to calculate sum
calculate_button = tk.Button(root, text="Calculate Sum", command=calculate_sum)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Run the Tkinter event loop
root.mainloop()

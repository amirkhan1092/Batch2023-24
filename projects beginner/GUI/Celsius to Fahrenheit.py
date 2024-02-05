import tkinter as tk
from tkinter import messagebox

def convert_to_fahrenheit():
    try:
        # Get the Celsius temperature from the entry widget
        celsius = float(entry.get())

        # Convert Celsius to Fahrenheit
        fahrenheit = (celsius * 9/5) + 32

        # Display the result in a message box
        messagebox.showinfo("Result", f"{celsius} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit.")
    except ValueError:
        # Display an error message if the input is not a valid number
        messagebox.showerror("Error", "Please enter a valid number for Celsius.")

# Create the main application window
root = tk.Tk()
root.title("Celsius to Fahrenheit Converter")

# Create a label for Celsius
celsius_label = tk.Label(root, text="Enter Celsius temperature:")
celsius_label.pack(pady=5)

# Create an entry widget for Celsius input
entry = tk.Entry(root, width=20)
entry.pack(pady=5)

# Create a button to trigger the conversion
convert_button = tk.Button(root, text="Convert", command=convert_to_fahrenheit)
convert_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()

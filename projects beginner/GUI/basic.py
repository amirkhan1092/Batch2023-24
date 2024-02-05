import tkinter as tk
from tkinter import messagebox

# Define a function to display a message based on user input
def display_message():
    user_input = entry.get()  # Get the user input from the entry widget
    message = "Hello, " + user_input + "!"  # Create a message to display
    messagebox.showinfo("Greetings", message)  # Display the message using a messagebox

# Create the main application window
root = tk.Tk()
root.title("Greetings App")

# Create a label widget to display instructions
label = tk.Label(root, text="Enter your name:")
label.pack()

# Create an entry widget for user input
entry = tk.Entry(root)
entry.pack()

# Create a button to trigger the display_message function
button = tk.Button(root, text="Submit", command=display_message)
button.pack()

# Run the Tkinter event loop
root.mainloop()

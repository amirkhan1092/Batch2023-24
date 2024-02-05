import tkinter as tk

def display_greeting():
    name = entry.get()
    greeting_message = f"Hello, {name}!"
    label_result.config(text=greeting_message)

# Create the main window
root = tk.Tk()
root.title("Greeting App")

# Create and place widgets
label_name = tk.Label(root, text="Enter your name:")
label_name.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

button_greet = tk.Button(root, text="Greet", command=display_greeting)
button_greet.pack(pady=10)

label_result = tk.Label(root, text="")
label_result.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()

import string
import random
import tkinter as tk
from tkinter import messagebox


class PasswordGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Generator")

        self.length_label = tk.Label(self, text="Length:")
        self.length_label.grid(row=0, column=0, padx=5, pady=5)

        self.length_entry = tk.Entry(self)
        self.length_entry.grid(row=0, column=1, padx=5, pady=5)

        self.complexity_label = tk.Label(self, text="Complexity:")
        self.complexity_label.grid(row=1, column=0, padx=5, pady=5)

        self.complexity_var = tk.StringVar()
        self.complexity_var.set("Weak")
        self.complexity_dropdown = tk.OptionMenu(self, self.complexity_var, "Weak", "Medium", "Strong")
        self.complexity_dropdown.grid(row=1, column=1, padx=5, pady=5)

        self.generate_button = tk.Button(self, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.password_label = tk.Label(self, text="Generated Password:")
        self.password_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

        self.password_output = tk.Label(self, text="")
        self.password_output.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

    def generate_password(self):
        length = int(self.length_entry.get())

        complexity = self.complexity_var.get()

        if complexity == "Weak":
            use_lowercase = True
            use_uppercase = False
            use_digits = False
            use_special = False
        elif complexity == "Medium":
            use_lowercase = True
            use_uppercase = True
            use_digits = True
            use_special = False
        elif complexity == "Strong":
            use_lowercase = True
            use_uppercase = True
            use_digits = True
            use_special = True
        else:
            messagebox.showerror("Error", "Invalid complexity level selected.")
            return

        characters = ''

        if use_lowercase:
            characters += string.ascii_lowercase
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_digits:
            characters += string.digits
        if use_special:
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "No characters selected for the password.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_output.config(text=password)


if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.mainloop()

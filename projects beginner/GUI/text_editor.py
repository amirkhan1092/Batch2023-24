import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import scrolledtext

class TextEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Text Editor")
        self.text_area = scrolledtext.ScrolledText(self.master, wrap=tk.WORD)
        self.text_area.pack(expand=True, fill='both')
        self.create_menu()

    def create_menu(self):
        menu_bar = tk.Menu(self.master)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_editor)
        menu_bar.add_cascade(label="File", menu=file_menu)

        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Cut", command=self.cut_text)
        edit_menu.add_command(label="Copy", command=self.copy_text)
        edit_menu.add_command(label="Paste", command=self.paste_text)
        edit_menu.add_separator()
        edit_menu.add_command(label="Select All", command=self.select_all_text)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        self.master.config(menu=menu_bar)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                self.text_area.delete('1.0', tk.END)
                self.text_area.insert(tk.END, file.read())

    def save_file(self):
        if not self.save_text():
            return
        with open(self.file_path, 'w') as file:
            file.write(self.text_area.get('1.0', tk.END))

    def save_as_file(self):
        self.file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if self.file_path:
            self.save_file()

    def exit_editor(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.master.destroy()

    def cut_text(self):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.text_area.get(tk.SEL_FIRST, tk.SEL_LAST))
        self.text_area.delete(tk.SEL_FIRST, tk.SEL_LAST)

    def copy_text(self):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.text_area.get(tk.SEL_FIRST, tk.SEL_LAST))

    def paste_text(self):
        self.text_area.insert(tk.INSERT, self.master.clipboard_get())

    def select_all_text(self):
        self.text_area.tag_add(tk.SEL, '1.0', tk.END)

    def save_text(self):
        if not hasattr(self, 'file_path'):
            self.file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            if not self.file_path:
                return False
        return True

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()

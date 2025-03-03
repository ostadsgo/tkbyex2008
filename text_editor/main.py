# Python text editor with Autocompelete and Syntax highlighting
# From book Tkinter by example by David Love
# Mon Mar  3 04:41:21 PM +0330 2025

import tkinter as tk
from tkinter import filedialog
from functools import partial


class Editor(tk.Tk):
    def __init__(self):
        super().__init__()

        self.FONT_SIZE = 12
        self.FONT_FAMILY = "Noto Sans"
        self.AUTOCOMPLETE_WORDS = [
            "def",
            "import",
            "if",
            "else",
            "while",
            "for",
            "try:",
            "except:",
            "print(",
            "True",
            "False",
        ]
        self.WINDOW_TITLE = "Text Editor"
        self.open_file = ""

        self.title(self.WINDOW_TITLE)
        self.geometry("800x600")

        # Menu
        self.menubar = tk.Menu(self, bg="lightgrey", fg="black")
        self.file_menu = tk.Menu(self.menubar, tearoff=0, bg="lightgrey", fg="black")
        self.file_menu.add_command(
            label="New", command=self.file_new, accelerator="Ctrl+N"
        )
        self.file_menu.add_command(
            label="Open", command=self.file_open, accelerator="Ctrl+O"
        )
        self.file_menu.add_command(
            label="Save", command=self.file_save, accelerator="Ctrl+S"
        )

        # File menu
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.configure(menu=self.menubar)

        # Main text area
        self.main_text = tk.Text(self, font=(self.FONT_FAMILY, self.FONT_SIZE))
        self.main_text.pack(expand=True, fill=tk.BOTH)

        # bind: Text area
        self.main_text.bind("<space>", self.destroy_autocomplete_menu)
        self.main_text.bind("<KeyRelease>", self.display_autocomplete_menu)
        self.main_text.bind("<Tab>", self.insert_space)

        # Bind: window
        self.bind("<Control-s>", self.file_save)
        self.bind("<Control-o>", self.file_open)
        self.bind("<Control-n>", self.file_new)

    def file_new(self, event=None):
        file_name = filedialog.asksaveasfilename()
        if file_name:
            self.open_file = file_name
            self.main_text.delete(1.0, tk.END)
            self.title(" - ".join([self.WINDOW_TITLE, self.open_file]))

    def file_open(self, event=None):
        file_to_open = filedialog.askopenfilename()
        if file_to_open:
            self.open_file = file_to_open
            self.main_text.delete(1.0, tk.END)

            with open(file_to_open, "r") as text_file:
                lines = text_file.readlines()
                if len(lines) > 0:
                    for index, line in enumerate(lines):
                        index = float(index) + 1.0
                        self.main_text.insert(index, line)
            self.title(" - ".join([self.WINDOW_TITLE, self.open_file]))



    def file_save(self, event=None):
        pass

    def destroy_autocomplete_menu(self, event=None):
        pass

    def display_autocomplete_menu(self, event=None):
        pass

    def insert_space(self, event=None):
        pass


if __name__ == "__main__":
    editor = Editor()
    editor.mainloop()

    def file_new(self, event=None):
        pass

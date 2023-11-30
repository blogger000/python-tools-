import os
import tkinter as tk
from tkinter import filedialog
from send2trash import send2trash

class FileRecycleApp:
    def __init__(self, master):
        self.master = master
        self.master.title("File Recycle and Delete")
        self.master.geometry("400x300")

        # File list
        self.file_listbox = tk.Listbox(self.master, selectmode=tk.MULTIPLE, height=10, width=50)
        self.file_listbox.pack(pady=10)

        # Buttons
        self.add_button = tk.Button(self.master, text="Add Files", command=self.add_files)
        self.add_button.pack(pady=5)

        self.recycle_button = tk.Button(self.master, text="Recycle", command=self.recycle_files)
        self.recycle_button.pack(pady=5)

        self.delete_button = tk.Button(self.master, text="Delete", command=self.delete_files)
        self.delete_button.pack(pady=5)

    def add_files(self):
        files = filedialog.askopenfilenames(title="Select Files", filetypes=[("All Files", "*.*")])
        for file in files:
            self.file_listbox.insert(tk.END, file)

    def recycle_files(self):
        selected_items = self.file_listbox.curselection()
        for index in reversed(selected_items):
            file_path = self.file_listbox.get(index)
            try:
                send2trash(file_path)
                self.file_listbox.delete(index)
                print(f"Sent '{file_path}' to the recycle bin.")
            except Exception as e:
                print(f"Error sending '{file_path}' to the recycle bin: {e}")

    def delete_files(self):
        selected_items = self.file_listbox.curselection()
        for index in reversed(selected_items):
            file_path = self.file_listbox.get(index)
            try:
                os.remove(file_path)
                self.file_listbox.delete(index)
                print(f"Deleted '{file_path}'.")
            except Exception as e:
                print(f"Error deleting '{file_path}': {e}")

# Create the main application window
root = tk.Tk()
app = FileRecycleApp(root)

# Run the application
root.mainloop()

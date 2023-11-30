import tkinter as tk
from cryptography.fernet import Fernet

class TextEncryptorDecryptor:
    def __init__(self, master):
        self.master = master
        self.master.title("Text Encryptor and Decryptor")
        self.master.geometry("400x300")

        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

        self.text_entry = tk.Text(self.master, height=8, width=40)
        self.text_entry.pack(pady=10)

        self.encrypt_button = tk.Button(self.master, text="Encrypt", command=self.encrypt_text)
        self.encrypt_button.pack(pady=5)

        self.decrypt_button = tk.Button(self.master, text="Decrypt", command=self.decrypt_text)
        self.decrypt_button.pack(pady=5)

        self.copy_button = tk.Button(self.master, text="Copy", command=self.copy_text)
        self.copy_button.pack(pady=5)

        self.paste_button = tk.Button(self.master, text="Paste", command=self.paste_text)
        self.paste_button.pack(pady=5)

    def encrypt_text(self):
        text_to_encrypt = self.text_entry.get("1.0", tk.END).strip().encode('utf-8')
        encrypted_text = self.cipher_suite.encrypt(text_to_encrypt)
        self.text_entry.delete("1.0", tk.END)
        self.text_entry.insert(tk.END, encrypted_text.decode('utf-8'))

    def decrypt_text(self):
        text_to_decrypt = self.text_entry.get("1.0", tk.END).strip().encode('utf-8')
        try:
            decrypted_text = self.cipher_suite.decrypt(text_to_decrypt)
            self.text_entry.delete("1.0", tk.END)
            self.text_entry.insert(tk.END, decrypted_text.decode('utf-8'))
        except Exception as e:
            print(f"Error decrypting text: {e}")

    def copy_text(self):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.text_entry.get("1.0", tk.END).strip())

    def paste_text(self):
        text_to_paste = self.master.clipboard_get()
        self.text_entry.delete("1.0", tk.END)
        self.text_entry.insert(tk.END, text_to_paste)

# Create the main application window
root = tk.Tk()
app = TextEncryptorDecryptor(root)

# Run the application
root.mainloop()

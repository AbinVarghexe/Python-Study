import tkinter as tk
from tkinter import messagebox


VALID_USERNAME = "admin"
VALID_PASSWORD = "python123"


def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if not username or not password:
        messagebox.showwarning("Missing Input", "Username and password cannot be empty.")
        return

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        messagebox.showinfo("Login", "Login Successful")
    else:
        messagebox.showerror("Login", "Invalid username or password.")


root = tk.Tk()
root.title("Login Form")
root.geometry("320x220")


tk.Label(root, text="Username:").pack(pady=(18, 4))
username_entry = tk.Entry(root, width=24)
username_entry.pack()

tk.Label(root, text="Password:").pack(pady=(12, 4))
password_entry = tk.Entry(root, width=24, show="*")
password_entry.pack()

tk.Button(root, text="Login", width=12, command=login).pack(pady=18)

root.mainloop()

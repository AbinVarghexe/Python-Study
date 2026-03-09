import tkinter as tk
from tkinter import messagebox


def check_strength():
    password = password_entry.get()

    if not password:
        messagebox.showwarning("Missing Input", "Please enter a password.")
        return

    has_length = len(password) >= 8
    has_digit = any(ch.isdigit() for ch in password)
    has_special = any(not ch.isalnum() for ch in password)

    score = has_length + has_digit + has_special

    if score <= 1:
        strength = "Weak"
    elif score == 2:
        strength = "Moderate"
    else:
        strength = "Strong"

    strength_var.set(strength)


root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("360x220")


tk.Label(root, text="Enter Password:").pack(pady=(16, 4))
password_entry = tk.Entry(root, width=26, show="*")
password_entry.pack()

tk.Button(root, text="Check Strength", command=check_strength).pack(pady=14)

tk.Label(root, text="Strength:").pack()
strength_var = tk.StringVar()
strength_entry = tk.Entry(root, textvariable=strength_var, width=20, state="readonly")
strength_entry.pack(pady=6)

root.mainloop()

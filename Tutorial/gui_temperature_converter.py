import tkinter as tk
from tkinter import messagebox


def convert_to_fahrenheit():
    try:
        celsius = float(celsius_entry.get())
        fahrenheit = (celsius * 9 / 5) + 32
        fahrenheit_var.set(f"{fahrenheit:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid Celsius value.")


root = tk.Tk()
root.title("Celsius to Fahrenheit")
root.geometry("360x220")


tk.Label(root, text="Temperature Converter", font=("Arial", 14)).pack(pady=10)

tk.Label(root, text="Celsius:").pack()
celsius_entry = tk.Entry(root, width=20)
celsius_entry.pack(pady=5)

tk.Button(root, text="Convert to Fahrenheit", command=convert_to_fahrenheit).pack(pady=8)

tk.Label(root, text="Fahrenheit:").pack()
fahrenheit_var = tk.StringVar()
fahrenheit_field = tk.Entry(root, textvariable=fahrenheit_var, width=20, state="readonly")
fahrenheit_field.pack(pady=5)

root.mainloop()

import tkinter as tk
from tkinter import messagebox


def generate_bill():
    try:
        item_price = float(price_entry.get())
        quantity = int(quantity_entry.get())

        if item_price < 0 or quantity < 0:
            raise ValueError

        subtotal = item_price * quantity
        discount = 0.10 * subtotal if subtotal > 1000 else 0
        final_amount = subtotal - discount

        output_var.set(
            f"Subtotal: {subtotal:.2f}  Discount: {discount:.2f}  Final Amount: {final_amount:.2f}"
        )
    except ValueError:
        messagebox.showerror("Invalid Input", "Enter valid values for price and quantity.")
        output_var.set("")


root = tk.Tk()
root.title("Bill Generator")
root.geometry("500x250")


tk.Label(root, text="Item Price:").pack(pady=(14, 4))
price_entry = tk.Entry(root, width=24)
price_entry.pack()

tk.Label(root, text="Quantity:").pack(pady=(10, 4))
quantity_entry = tk.Entry(root, width=24)
quantity_entry.pack()

tk.Button(root, text="Generate Bill", command=generate_bill).pack(pady=14)

output_var = tk.StringVar()
output_entry = tk.Entry(root, textvariable=output_var, width=62, state="readonly")
output_entry.pack(pady=6)

root.mainloop()

import tkinter as tk


def clear_label():
    title_label.config(text="")
    clear_button.config(state=tk.DISABLED)
    restore_button.config(state=tk.NORMAL)


def restore_label():
    title_label.config(text="Python GUI Demo")
    restore_button.config(state=tk.DISABLED)
    clear_button.config(state=tk.NORMAL)


root = tk.Tk()
root.title("Label Demo")
root.geometry("320x160")


title_label = tk.Label(root, text="Python GUI Demo", font=("Arial", 16))
title_label.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack()

clear_button = tk.Button(button_frame, text="Clear", width=10, command=clear_label)
clear_button.grid(row=0, column=0, padx=8)

restore_button = tk.Button(
    button_frame,
    text="Restore",
    width=10,
    command=restore_label,
    state=tk.DISABLED,
)
restore_button.grid(row=0, column=1, padx=8)

root.mainloop()

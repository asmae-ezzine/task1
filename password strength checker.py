import tkinter as tk
from tkinter import messagebox
import re

# Function to check the password strength.
def check_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"\d", password):
        strength += 1
    if re.search(r"[\W_]", password):
        strength += 1

    if strength == 5:
        return "Strong"
    elif strength >= 3:
        return "Medium"
    else:
        return "Weak"

# Function to update the password strength label.
def update_password_strength(event):
    password = password_entry.get()
    strength = check_password_strength(password)
    strength_label.config(text=strength)
    if strength == "Strong":
        strength_label.config(fg="green")
    elif strength == "Medium":
        strength_label.config(fg="orange")
    else:
        strength_label.config(fg="red")

# Create the graphical user interface.
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("300x150")

password_label = tk.Label(root, text="Password:")
password_label.pack(pady=5)

password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)
password_entry.bind("<KeyRelease>", update_password_strength)

strength_label = tk.Label(root, text="", font=("Helvetica", 14))
strength_label.pack(pady=5)

exit_btn = tk.Button(root, text="Quit", command=root.quit)
exit_btn.pack(pady=10)

root.mainloop()

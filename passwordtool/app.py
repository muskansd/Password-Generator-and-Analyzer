import tkinter as tk
from tkinter import messagebox
import re
import random
import string

# ------------------------
# Password Analyzer Logic
# ------------------------
def password_strength(password):
    score = 0
    if len(password) >= 8: score += 1
    if re.search(r'[a-z]', password): score += 1
    if re.search(r'[A-Z]', password): score += 1
    if re.search(r'[0-9]', password): score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password): score += 1

    if score <= 2:
        return "Weak", "red", 40
    elif score == 3:
        return "Moderate", "orange", 60
    elif score == 4:
        return "Strong", "blue", 80
    else:
        return "Very Strong", "green", 100

# ------------------------
# Password Generator Logic
# ------------------------
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>/?"
    return ''.join(random.choice(chars) for _ in range(length))

# ------------------------
# GUI Functions
# ------------------------
def analyze_password(event=None):
    pwd = password_entry.get()
    strength, color, percent = password_strength(pwd)
    strength_label.config(text=strength, fg=color)
    strength_bar.config(width=percent*2, bg=color)  # multiply by 2 for better visual

def generate_new_password():
    pwd = generate_password()
    password_entry.delete(0, tk.END)
    password_entry.insert(0, pwd)
    analyze_password()

def copy_to_clipboard():
    pwd = password_entry.get()
    if pwd:
        root.clipboard_clear()
        root.clipboard_append(pwd)
        messagebox.showinfo("Copied!", "Password copied to clipboard.")
    else:
        messagebox.showwarning("Empty", "No password to copy!")

def toggle_password():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        view_btn.config(text='View Password')
    else:
        password_entry.config(show='')
        view_btn.config(text='Hide Password')

# ------------------------
# GUI Setup
# ------------------------
root = tk.Tk()
root.title("Password Tool")
root.geometry("480x320")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="Password Strength Analyzer & Generator", font=("Arial", 14))
title_label.pack(pady=10)

# Frame for password label + entry + view button
password_frame = tk.Frame(root)
password_frame.pack(pady=10)

# Label on left
password_label = tk.Label(password_frame, text="Enter Password:", font=("Arial", 12))
password_label.grid(row=0, column=0, padx=5)

# Password Entry
password_entry = tk.Entry(password_frame, font=("Arial", 12), width=25, show="*")
password_entry.grid(row=0, column=1, padx=5)
password_entry.bind("<KeyRelease>", analyze_password)

# View Password Button
view_btn = tk.Button(password_frame, text="View Password", command=toggle_password, width=12)
view_btn.grid(row=0, column=2, padx=5)

# Strength Bar
strength_frame = tk.Frame(root, width=280, height=20, bg="#ddd")
strength_frame.pack(pady=5)
strength_bar = tk.Frame(strength_frame, width=0, height=20, bg="red")
strength_bar.pack()

# Strength Label
strength_label = tk.Label(root, text="Enter password", font=("Arial", 12))
strength_label.pack(pady=5)

# Buttons
generate_btn = tk.Button(root, text="Generate Password", command=generate_new_password, width=20, bg="#007bff", fg="white")
generate_btn.pack(pady=5)

copy_btn = tk.Button(root, text="Copy Password", command=copy_to_clipboard, width=20, bg="#28a745", fg="white")
copy_btn.pack(pady=5)

# Start GUI loop
root.mainloop()

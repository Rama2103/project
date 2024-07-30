import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from styles import apply_styles

def on_check():
    password = entry.get()
    result = check_password_strength(password)
    messagebox.showinfo("Password Strength Check", result)

def check_password_strength(password):
    min_length = 8
    if len(password) < min_length:
        return "Password must be at least 8 characters long."
    if not any(c.isupper() for c in password):
        return "Password must contain at least one uppercase letter."
    if not any(c.islower() for c in password):
        return "Password must contain at least one lowercase letter."
    if not any(c.isdigit() for c in password):
        return "Password must contain at least one digit."
    if not any(c in "!@#$%^&*(),.?\":{}|<>" for c in password):
        return "Password must contain at least one special character."
    return "Password is strong.\n the password is " + password

app = tk.Tk()
app.title("Password Checker")
apply_styles(app)

app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)
app.grid_rowconfigure(2, weight=1)
app.grid_columnconfigure(0, weight=1)

frame = ttk.Frame(app, padding="20")
frame.grid(row=0, column=0, sticky='nsew')

frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)
frame.grid_rowconfigure(2, weight=1)
frame.grid_columnconfigure(0, weight=1)

label = ttk.Label(frame, text="Enter a password:")
label.grid(row=0, column=0, pady=10, sticky='nsew')

entry = ttk.Entry(frame, show="*", width=30)
entry.grid(row=1, column=0, pady=10, sticky='nsew')

check_button = ttk.Button(frame, text="Check", command=on_check)
check_button.grid(row=2, column=0, pady=10, sticky='nsew')

app.mainloop()


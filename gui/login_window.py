import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from gui.register_window import show_register
from database.db import Session
from database.models import User
from utils.encryption import check_password

def show_login():
    root = tk.Tk()
    root.title("Sudoku - Login")

    window_width = 300
    window_height = 250
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    ttk.Label(root, text = "Email: ").pack(pady = 5)
    email_entry = ttk.Entry(root)
    email_entry.pack()

    ttk.Label(root, text = "Password: ").pack(pady = 5)
    password_entry = ttk.Entry(root, show = "*")
    password_entry.pack()

    def login():
        email = email_entry.get().strip()
        password = password_entry.get()

        db = Session()
        user = db.query(User).filter_by(email = email).first()
        db.close()

        if not user:
            messagebox.showerror("Error", "User not found!")
            return
        if not check_password(password, user.hashed_password):
            messagebox.showerror("Error", "Incorrect password!")
            return
        
        messagebox.showinfo("Success",f"Login successful, welcome {user.username}!")
        root.destroy()

        from gui.settings_window import show_settings
        show_settings(user)

    ttk.Button(root, text = "Log In", command = login).pack(pady = 10)
    ttk.Button(root, text = "Sign Up", command = show_register).pack(pady = 5)

    root.mainloop()
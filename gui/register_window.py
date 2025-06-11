import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from database.db import Session
from database.models import User
from utils.encryption import hash_password

def show_register():
    window = tk.Toplevel()
    window_width = 350
    window_height = 400
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    window.title("Register Window")
    
    fields = {}

    def add_field(label, key, show = None):
        ttk.Label(window, text = label).pack(pady = 5)
        entry = ttk.Entry(window, show = show)
        entry.pack()
        fields[key] = entry

    add_field("Email: ", "email")
    add_field("Username: ", "username")
    add_field("Date of Birth (YYYY-MM-DD): ", "date_of_birth")
    add_field("Password: ", "password", show = "*")
    add_field("Confirm Password: ", "confirm_password", show = "*")


    def register():
        email = fields["email"].get().strip()
        username = fields["username"].get().strip()
        date_of_birth = fields["date_of_birth"].get().strip()
        password = fields["password"].get()
        confirm_password = fields["confirm_password"].get()

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return
        
        try:
            birthdate = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
        except ValueError:
            messagebox.showerror("Error", "Invalid date format! Use YYYY-MM-DD.")
            return 
        
        db = Session()
        if db.query(User).filter((User.email == email) | (User.username == username)).first():
            messagebox.showerror("Error", "Email or Username already exists!")
            return
        
        new_user = User(
            email = email,
            username = username,
            date_of_birth = birthdate,
            hashed_password = hash_password(password)
        )

        db.add(new_user)
        db.commit()
        db.close()
        messagebox.showinfo("Success", "Registration successful!")
        window.destroy()
    
    ttk.Button(window, text = "Register", command = register).pack(pady = 20)

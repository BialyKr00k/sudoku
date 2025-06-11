import tkinter as tk
from gui.login_window import show_login
from database.db import init_db

def main():
    init_db()

    root = tk.Tk()
    root.withdraw() 
    show_login()
    root.mainloop()

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import ttk


def show_settings(user):
    window = tk.Tk()
    window.title("Settings")

    window_width = 300
    window_height = 200
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    ttk.Label(window, text = "Choose level of difficulty:").pack(pady = 10)

    def select_level(level):
        window.destroy()
        from gui.game_window import start_game
        start_game(user, level)
    
    ttk.Button(window, text="Easy", command=lambda: select_level("easy")).pack(pady=5)
    ttk.Button(window, text="Medium", command=lambda: select_level("medium")).pack(pady=5)
    ttk.Button(window, text="Hard", command=lambda: select_level("hard")).pack(pady=5)

    window.mainloop()
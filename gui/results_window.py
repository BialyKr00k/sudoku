import tkinter as tk
from tkinter import ttk, messagebox
from database.db import Session
from database.models import GameResult
from export.pdf_exporter import export_results_pdf  # <- Upewnij się, że ta funkcja zwraca ścieżkę

def show_results(user, level):
    root = tk.Tk()
    root.title(f"Score - {level.capitalize()}")

    window_width = 500
    window_height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    ttk.Label(root, text=f"Score for {user.username} - {level.capitalize()}").pack(pady=10)

    db = Session()
    results = (db.query(GameResult)
                  .filter_by(user_id=user.id, difficulty=level)
                  .order_by(GameResult.score.desc()).all())
    db.close()

    columns = ("Score", "Time [s]", "Date")
    tree = ttk.Treeview(root, columns=columns, show='headings')

    for col in columns:
        tree.heading(col, text=col)

    for result in results:
        tree.insert("", tk.END, values=(
            result.score,
            result.time_seconds,
            result.timestamp.strftime("%Y-%m-%d %H:%M")
        ))

    tree.pack(expand=True, fill='both', padx=10, pady=10)

    def export_pdf():
        try:
            path = export_results_pdf(user, level)
            messagebox.showinfo("PDF Zapisany", f"Wyniki zapisano do:\n{path}")
        except Exception as e:
            messagebox.showerror("Błąd", f"Nie udało się zapisać PDF:\n{str(e)}")

    ttk.Button(root, text="Eksportuj do PDF", command=export_pdf).pack(pady=10)

    root.mainloop()

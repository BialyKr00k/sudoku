import tkinter as tk
from gui.login_window import show_login
from database.db import init_db, Session
from database.models import SudokuBoard
from logic.sudoku_generator import add_sample_boards

def main():
    # Inicjalizacja bazy danych
    init_db()

    # Sprawdzenie czy są już plansze
    session = Session()
    has_boards = session.query(SudokuBoard).count() > 0
    session.close()

    # Dodanie przykładowych plansz tylko jeśli ich nie ma
    if not has_boards:
        add_sample_boards()

    # Uruchomienie GUI
    root = tk.Tk()
    root.withdraw()
    show_login()
    root.mainloop()

if __name__ == "__main__":
    main()

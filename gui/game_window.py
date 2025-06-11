import tkinter as tk
from tkinter import ttk, messagebox
from database.db import Session
from database.models import SudokuBoard, GameResult
from logic.score_manager import ScoreManager
from gui.results_window import show_results
import random

def start_game(user, level):
    window = tk.Tk()
    window.title(f"Sudoku - {level.capitalize()}")

    window_width = 500
    window_height = 550
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    db = Session()
    board = db.query(SudokuBoard).filter_by(difficulty=level).first()
    if not board:
        messagebox.showerror("Błąd", f"Nie znaleziono planszy dla poziomu '{level}'")
        window.destroy()
        return

    sm = ScoreManager(board.solution_data)
    db.close()

    info_frame = ttk.Label(window)
    info_frame.pack(pady=10)

    score_label = ttk.Label(info_frame, text=f"Score: {sm.score}")
    score_label.pack(side='left', padx=20)
    time_label = ttk.Label(info_frame, text="Time: 0s")
    time_label.pack(side='right', padx=20)

    timer_id = None
    hint_update_id = None

    def update_timer():
        nonlocal timer_id
        time_label.config(text=f"Time: {sm.elapsed_time()}s")
        timer_id = window.after(1000, update_timer)
    update_timer()

    entries = []
    used_hints = 0
    max_hints = 3

    frame_grid = ttk.Frame(window)
    frame_grid.pack(expand=True)

    for i in range(9):
        row = []
        for j in range(9):
            idx = i * 9 + j
            ch = board.board_data[idx]

            e = tk.Entry(frame_grid, width=2, justify='center', font=('Arial', 16),
                         bg='white', relief='solid', bd=1)
            padx = (4 if j % 3 == 0 else 1, 1)
            pady = (4 if i % 3 == 0 else 1, 1)
            e.grid(row=i + 1, column=j, padx=padx, pady=pady)

            if ch != '0':
                e.insert(0, ch)
                e.config(state='disabled')
            else:
                def handler(event, idx=idx, entry=e):
                    if entry['state'] == 'disabled':
                        return
                    val = entry.get().strip()
                    if not val.isdigit() or not (1 <= int(val) <= 9):
                        entry.delete(0, tk.END)
                        return

                    i, j = idx // 9, idx % 9
                    entered = int(val)
                    correct_solution = sm.solution[idx]

                    if entered == correct_solution:
                        sm.score += 100
                        entry.config(foreground='green', state='disabled')
                        score_label.config(text=f"Score: {sm.score}")
                        check_completion()
                        return

                    row_vals = [entries[i][x].get() for x in range(9) if x != j and entries[i][x].get().isdigit()]
                    col_vals = [entries[y][j].get() for y in range(9) if y != i and entries[y][j].get().isdigit()]
                    block_vals = []
                    bi, bj = 3 * (i // 3), 3 * (j // 3)
                    for x in range(bi, bi + 3):
                        for y in range(bj, bj + 3):
                            if x == i and y == j:
                                continue
                            v = entries[x][y].get()
                            if v.isdigit():
                                block_vals.append(v)

                    conflict = (str(entered) in row_vals or
                                str(entered) in col_vals or
                                str(entered) in block_vals)
                    if conflict:
                        entry.config(foreground='red')
                    else:
                        sm.score -= 25
                        entry.config(foreground='red')

                    score_label.config(text=f"Score: {sm.score}")
                    check_completion()

                e.bind("<Return>", handler)
            row.append(e)
        entries.append(row)

    def check_completion():
        all_filled = all(e.get().isdigit() for row in entries for e in row)
        if all_filled:
            end_game()

    def end_game():
        if timer_id:
            window.after_cancel(timer_id)
        if hint_update_id:
            window.after_cancel(hint_update_id)

        elapsed = sm.elapsed_time()
        db2 = Session()
        result = GameResult(
            user_id=user.id,
            difficulty=level,
            score=sm.score,
            time_seconds=elapsed
        )
        db2.add(result)
        db2.commit()
        db2.close()
        messagebox.showinfo("Congratulations!", f"Your score: {sm.score}, Time: {elapsed}s")
        window.destroy()
        show_results(user, level)

        again = messagebox.askyesno("Play Again", "Do you want to play again?")
        if again:
            start_game(user, level)

    def give_hint():
        nonlocal used_hints
        if used_hints >= max_hints:
            messagebox.showinfo("Hint", "You have used all your hints.")
            return

        empty_cells = [(i, j) for i in range(9) for j in range(9) if entries[i][j].get() == '']
        if not empty_cells:
            return

        i, j = random.choice(empty_cells)
        idx = i * 9 + j
        correct = sm.solution[idx]
        entries[i][j].delete(0, tk.END)
        entries[i][j].insert(0, str(correct))
        entries[i][j].config(state='disabled', foreground='blue')
        sm.score += 50
        used_hints += 1
        score_label.config(text=f"Score: {sm.score}")
        check_completion()

    hint_button = ttk.Button(window, text="Hint (3 left)", command=give_hint)
    hint_button.pack(pady=10)

    def update_hint_text():
        nonlocal hint_update_id
        hint_button.config(text=f"Hint ({max_hints - used_hints} left)")
        hint_update_id = window.after(500, update_hint_text)
    update_hint_text()

    window.mainloop()

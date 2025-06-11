# 🧠 Sudoku

Gra Sudoku z interaktywnym GUI w Pythonie (Tkinter), systemem punktów, rankingiem i eksportem wyników do PDF. Gotowa do uruchomienia jednym poleceniem!

🚀 Jak uruchomić?

    Pobierz repozytorium z GitHuba:

        git clone https://github.com/twoj-login/sudoku-brain.git
        cd sudoku-brain

    Uruchom aplikację:

        python main.py

📦 Wszystkie biblioteki są wbudowane w requirements.txt, a domyślna baza danych tworzy się automatycznie (sqlite).

🎮 Funkcje gry

    Wybór poziomu trudności (easy / medium / hard)

    Weryfikacja poprawności w czasie rzeczywistym

    Kolory pól (zielony – poprawny, czerwony – błąd)

    System punktów (poprawna liczba: +100, zła: -25)

    Zegar czasu gry ⏱️

    Podświetlenie bloków 3x3 grubszymi liniami

    Przycisk Hint (x3) – podpowiedzi (50 pkt za każdą)

    Zakończenie gry + zapis wyniku

    Podgląd wyników i eksport do PDF (do katalogu Pobrane)

📁 Struktura projektu

sudoku-brain/
│
├── database/
│   ├── db.py               # Połączenie z bazą danych SQLite
│   └── models.py           # Modele: User, GameResult, SudokuBoard
│
├── gui/
│   ├── game_window.py      # Główne okno gry
│   ├── login_window.py     # Logowanie / rejestracja
│   ├── settings_window.py  # Wybór poziomu
│   └── results_window.py   # Wyniki + eksport do PDF
│
├── logic/
│   ├── score_manager.py    # System punktów i czasu
│   └── encryption.py       # Haszowanie haseł (bcrypt)
│
├── export/
│   └── pdf_exporter.py     # Eksport wyników do PDF
│
├── sudoku.db               # Plik bazy danych SQLite (tworzy się automatycznie)
├── requirements.txt        # Biblioteki projektu
└── main.py                 # Punkt startowy aplikacji

✅ Wymagania

    Python 3.10+ (zalecane: 3.12)

    Brak potrzeby ręcznej instalacji – wszystkie biblioteki są domyślne lub w requirements.txt

📄 Licencja

    Projekt stworzony jako aplikacja edukacyjna. Możesz modyfikować i rozwijać wedle uznania.
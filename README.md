# 🧠 Sudoku

Gra Sudoku z interaktywnym GUI w Pythonie (Tkinter), systemem punktów, rankingiem i eksportem wyników do PDF. Gotowa do uruchomienia jednym poleceniem!

🚀 Jak uruchomić?

    Pobierz repozytorium z GitHuba:

        git clone https://github.com/twoj-login/sudoku-brain.git
        cd sudoku-brain

    Uruchom aplikację:
        1.otwórz terminal
        2. jesli nie masz virtualenv: pip install virtualenv
        3.komenda: python -m venv venv
        4.aktywuj venv: venv\Scripts\activate
        5.pip install -r requirements.txt
        6. komenda: python main.py

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

✅ Wymagania

    Python 3.10+ (zalecane: 3.12)

    Brak potrzeby ręcznej instalacji – wszystkie biblioteki są domyślne lub w requirements.txt

📄 Licencja

    Projekt stworzony jako aplikacja edukacyjna. Możesz modyfikować i rozwijać wedle uznania.

import time
import tkinter as tk
from threading import Thread

def flash_black_screen(duration_ms=50):
    """
    Funkcja tworzy okno pełnoekranowe z czarnym tłem,
    które wyświetla się przez duration_ms milisekund (domyślnie 50 ms).
    """
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.configure(bg="black")
    root.after(duration_ms, root.destroy)
    root.mainloop()

def wait_for_full_minutes():
    """
    Funkcja uruchamia miganie czarnym ekranem dokładnie o pełnych minutach.
    Jeśli skrypt zostanie uruchomiony w trakcie minuty, odczeka do najbliższej pełnej minuty,
    a potem będzie co 60 sekund uruchamiać miganie.
    """
    # Początkowe odczekanie do najbliższej pełnej minuty
    print("halo")
    now = time.time()
    remainder = now % 60
    if remainder < 0.01:
        # Jeżeli dokładnie pełna minuta – migaj od razu i potem odczekaj 60 sekund
        Thread(target=flash_black_screen).start()
        time.sleep(60)
    else:
        # Odczekaj do momentu, gdy sekundy osiągną 0
        time.sleep(60 - remainder)
    
    # Następnie cyklicznie, co 60 sekund
    while True:
        Thread(target=flash_black_screen).start()
        time.sleep(60)

if __name__ == "__main__":
    wait_for_full_minutes()

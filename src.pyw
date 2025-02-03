import time
import tkinter as tk

def flash_black_screen(root, duration_ms=50):
    """Wyświetla migający czarny ekran jako okno potomne"""
    flash = tk.Toplevel(root)
    flash.attributes("-fullscreen", True)
    flash.overrideredirect(True)
    flash.attributes("-topmost", True)
    flash.configure(bg="black")
    flash.after(duration_ms, flash.destroy)

def schedule_flash(root):
    """Planowanie migania na początku każdej minuty"""
    now = time.time()
    next_minute = (int(now // 60) + 1) * 60
    delay_ms = int((next_minute - now) * 1000)
    root.after(delay_ms, lambda: trigger_flash(root))

def trigger_flash(root):
    """Wywołuje miganie i restartuje harmonogram"""
    flash_black_screen(root)
    schedule_flash(root)

def create_status_window():
    """Tworzy główne okno z animowanym wskaźnikiem czasu"""
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes("-topmost", True)

    # Konfiguracja przezroczystości
    bg_color = "#F7F7F7"
    arc_color = "#FF3B30"
    root.configure(bg=bg_color)
    root.wm_attributes("-transparentcolor", bg_color)

    # Pozycja i rozmiar okna
    win_size = 30
    root.geometry(f"{win_size}x{win_size}+{root.winfo_screenwidth()-win_size-10}+10")

    # Animowany wskaźnik
    canvas = tk.Canvas(root, width=win_size, height=win_size, bg=bg_color, highlightthickness=0)
    canvas.pack()
    
    padding = 4
    arc = canvas.create_arc(padding, padding, win_size-padding, win_size-padding,
                          start=90, style="arc", outline=arc_color, width=6)

    def update_indicator():
        czas = time.localtime()
        sekundy = czas.tm_sec
        procent = (60 - sekundy) / 60
        canvas.itemconfig(arc, extent=-procent*360)
        root.after(100, update_indicator)

    update_indicator()
    return root

if __name__ == "__main__":
    main_window = create_status_window()
    schedule_flash(main_window)
    main_window.mainloop()
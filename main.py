import os
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

import yt_dlp

## TODO: varsayilan yol masaustu olacak
## TODO: klasor sec dugmeleri ve input arasindaki boslugu arttir



def create_ui(root: tk.Tk) -> None:
    root.title("YouTube MP3 Converter")
    root.geometry("600x260")
    root.resizable(False, False)

    # State variables
    root.url_var = tk.StringVar()
    root.folder_var = tk.StringVar(value=os.path.expanduser("~"))
    root.status_var = tk.StringVar(value="Hazır")
    root.progress_var = tk.DoubleVar(value=0.0)

    main_frame = ttk.Frame(root, padding=16)
    main_frame.pack(fill="both", expand=True)

    # URL row
    ttk.Label(main_frame, text="YouTube URL:").grid(row=0, column=0, sticky="w")
    url_entry = ttk.Entry(main_frame, textvariable=root.url_var, width=55)
    url_entry.grid(row=1, column=0, columnspan=3, sticky="we", pady=(4, 8))
    url_entry.focus()

    # Folder selection
    ttk.Label(main_frame, text="Kayıt klasörü:").grid(row=2, column=0, sticky="w")
    folder_label = ttk.Label(
        main_frame,
        textvariable=root.folder_var,
        relief="sunken",
        anchor="w",
    )
    folder_label.grid(row=3, column=0, columnspan=2, sticky="we", pady=(4, 8))

    select_btn = ttk.Button(
        main_frame,
        text="Klasör Seç",
        command=lambda: select_folder(root),
        width=14,
    )
    select_btn.grid(row=3, column=2, sticky="e")

    # Progress bar
    ttk.Label(main_frame, text="İlerleme:").grid(row=4, column=0, sticky="w")
    progress = ttk.Progressbar(
        main_frame,
        variable=root.progress_var,
        maximum=100,
        mode="determinate",
    )
    progress.grid(row=5, column=0, columnspan=3, sticky="we", pady=(4, 8))

    # Status text
    status_label = ttk.Label(
        main_frame,
        textvariable=root.status_var,
        anchor="w",
        foreground="#555",
    )
    status_label.grid(row=6, column=0, columnspan=3, sticky="we", pady=(0, 8))

    # Download button
    root.download_btn = ttk.Button(
        main_frame,
        text="MP3 Olarak İndir",
        command=lambda: start_download_thread(root),
        width=20,
    )
    root.download_btn.grid(row=7, column=0, columnspan=3, pady=(4, 0))

    # Layout config
    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=0)
    main_frame.columnconfigure(2, weight=0)


def select_folder(root: tk.Tk) -> None:
    folder = filedialog.askdirectory(
        title="Kayıt klasörü seç",
        initialdir=root.folder_var.get() or os.path.expanduser("~"),
    )
    if folder:
        root.folder_var.set(folder)


def start_download_thread(root: tk.Tk) -> None:
    url = root.url_var.get().strip()
    folder = root.folder_var.get().strip()

    if not url:
        messagebox.showwarning("Uyarı", "Lütfen bir YouTube URL'si girin.")
        return

    if not folder:
        messagebox.showwarning("Uyarı", "Lütfen bir kayıt klasörü seçin.")
        return

    # Disable button while downloading
    root.download_btn.config(state="disabled")
    root.progress_var.set(0.0)
    root.status_var.set("İndirme başlatılıyor...")

    thread = threading.Thread(
        target=download_audio,
        args=(root, url, folder),
        daemon=True,
    )
    thread.start()


def download_audio(root: tk.Tk, url: str, folder: str) -> None:
    def update_status(text: str) -> None:
        root.after(0, lambda: root.status_var.set(text))

    def update_progress(percent: float) -> None:
        root.after(0, lambda: root.progress_var.set(max(0.0, min(100.0, percent))))

    def enable_button() -> None:
        root.after(0, lambda: root.download_btn.config(state="normal"))

    def progress_hook(d: dict) -> None:
        if d.get("status") == "downloading":
            total = d.get("total_bytes") or d.get("total_bytes_estimate")
            downloaded = d.get("downloaded_bytes", 0)
            if total:
                percent = downloaded / total * 100
                update_progress(percent)
            update_status("İndiriliyor...")
        elif d.get("status") == "finished":
            update_status("Ses dönüştürülüyor...")
            update_progress(100.0)

    ydl_opts = {
        "format": "bestaudio/best",
        'noplaylist': True,  # Masaüstünün dolmasını engelleyen kritik ayar
        "outtmpl": os.path.join(folder, "%(title)s.%(ext)s"),
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "progress_hooks": [progress_hook],
        # Quiet terminal output; we show UI status instead
        "quiet": True,
        "no_warnings": True,
    }

    try:
        update_status("İndirme başlatılıyor...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        update_status("Tamamlandı.")
        messagebox.showinfo("Başarılı", "MP3 indirme tamamlandı.")
    except Exception as exc:  # pylint: disable=broad-except
        update_status("Hata oluştu.")
        messagebox.showerror("Hata", f"İndirme sırasında bir hata oluştu:\n{exc}")
    finally:
        enable_button()


def main() -> None:
    root = tk.Tk()
    create_ui(root)
    root.mainloop()


if __name__ == "__main__":
    main()


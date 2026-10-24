from pathlib import Path
from tkinter import Tk, filedialog
import yt_dlp

def choose_folder():
    """Открывает окно выбора папки. При отмене возвращает пустую строку."""
    root = Tk()
    root.withdraw()
    folder = filedialog.askdirectory(
        title="Куда сохранить видео?",
        initialdir=str(Path.home()),
    )
    root.destroy()
    return folder

url = input("Ссылка: ")
folder = choose_folder()

if not folder:
    print("Отменено.")
    raise SystemExit

opts = {
    "format": "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]/b",
    "merge_output_format": "mp4",
    "paths": {"home": folder},
}

try:
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([url])
    print(f"Готово! Сохранено в: {folder}")
except yt_dlp.utils.DownloadError:
    print("Не получилось скачать. Проверь ссылку.")
import subprocess
from pathlib import Path
from tkinter import Tk, filedialog

import yt_dlp


def default_video_dir():
    """Папка «Видео» пользователя на любом языке системы."""
    try:
        result = subprocess.run(
            ["xdg-user-dir", "VIDEOS"],
            capture_output=True, text=True, check=True,
        )
        path = Path(result.stdout.strip())
        if path != Path.home():
            return path
    except (FileNotFoundError, subprocess.CalledProcessError):
        pass
    return Path.home() / "Videos"


def choose_folder():
    """Открывает окно выбора папки. При отмене возвращает пустую строку."""
    root = Tk()
    root.withdraw()
    folder = filedialog.askdirectory(
        title="Куда сохранить видео?",
        initialdir=str(default_video_dir()),
    )
    root.destroy()
    return folder


url = input("Ссылка: ")
folder = choose_folder()

save_dir = Path(folder) if folder else default_video_dir()
save_dir.mkdir(parents=True, exist_ok=True)

opts = {
    "format": "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]/b",
    "merge_output_format": "mp4",
    "paths": {"home": str(save_dir)},
}

try:
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([url])
    print(f"Готово! Сохранено в: {save_dir}")
except yt_dlp.utils.DownloadError:
    print("Не получилось скачать. Проверь ссылку.")
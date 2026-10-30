# mediafetcher

Простая качалка видео с YouTube на Python. Сохраняет видео в mp4.

## Требования
- Python 3.10+
- ffmpeg (для склейки видео и звука)
  - Fedora: `sudo dnf install ffmpeg`
  - Ubuntu/Debian: `sudo apt install ffmpeg`
  - Windows: `winget install Gyan.FFmpeg`
- tkinter (для окна выбора папки)
  - Fedora: `sudo dnf install python3-tkinter`
  - Ubuntu/Debian: `sudo apt install python3-tk`
  - Windows: уже входит в Python с python.org

## Установка
```bash
git clone https://github.com/dayvoens/mediafetcher.git
cd mediafetcher
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Запуск
```bash
python main.py
```
Вставь ссылку и выбери папку. Если нажать «Отмена», скачивание отменится.

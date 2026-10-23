# mediafetcher

Простая качалка видео с YouTube на Python. Сохраняет видео в mp4.

## Требования
- Python 3.10+
- ffmpeg (для склейки видео и звука)
  - Fedora: `sudo dnf install ffmpeg`
  - Ubuntu/Debian: `sudo apt install ffmpeg`
  - Windows: `winget install Gyan.FFmpeg`

## Установка
```bash
git clone https://github.com/dayvoens/ytgrab.git
cd ytgrab
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activates
pip install -r requirements.txt
```

## Запуск
```bash
python main.py
```
Вставь ссылку и выбери папку. Если нажать «Отмена», видео сохранится в папку «Видео».
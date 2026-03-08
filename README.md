## YouTube MP3 Converter

YouTube MP3 Converter is a small desktop application that lets you quickly **download YouTube videos as MP3 files** to your computer.

### Features

- **GUI**: Simple, modern interface built with `tkinter` and `ttk`
- **YouTube → MP3 conversion**: Uses `yt-dlp` and `ffmpeg` to extract the best audio stream as MP3
- **Progress tracking**: Progress bar and status text show download and conversion state
- **Folder selection**: Downloads to the desktop by default, or to any folder you choose

### Tech stack

- **Python 3**
- **tkinter / ttk** – desktop UI
- **yt-dlp** – YouTube download and audio extraction
- **ffmpeg** – audio conversion (to MP3)

### Installation

```bash
cd python/mp3_converter
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

`yt-dlp` requires **ffmpeg** to be installed on your system for MP3 conversion:

- macOS: `brew install ffmpeg`
- Linux: `sudo apt install ffmpeg` (or your distro’s equivalent)
- Windows: download ffmpeg and add it to your `PATH`

### Run & usage

```bash
python main.py
```

- Paste a YouTube video URL into the top input field.
- Use `Klasör Seç` (Select Folder) to pick the output directory (defaults to Desktop).
- Click `MP3 Olarak İndir` (Download as MP3) to start.
- The progress bar and status text will show the current state; a message box appears when the process finishes.


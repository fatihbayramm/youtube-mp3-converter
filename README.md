## YouTube MP3 Converter

Bu küçük masaüstü uygulaması, YouTube videolarını MP3 formatında indirmenizi sağlar.  
Arayüz `tkinter`, indirme işlemi ise `yt-dlp` kütüphanesi ile yapılır.

### Kurulum

```bash
cd python/mp3_converter
python -m venv .venv
source .venv/bin/activate  # Windows için: .venv\Scripts\activate
pip install -r requirements.txt
```

`yt-dlp` MP3 dönüştürme için sisteminizde `ffmpeg` kurulu olmasını ister:

- **macOS**: `brew install ffmpeg`
- **Linux**: Paket yöneticiniz ile `ffmpeg` kurun (`sudo apt install ffmpeg` vb.)
- **Windows**: `ffmpeg` indirip PATH değişkenine ekleyin.

### Çalıştırma

```bash
python main.py
```

### Kullanım

- YouTube video URL'sini metin kutusuna yapıştırın.
- `Klasör Seç` butonu ile MP3 dosyasının kaydedileceği klasörü belirleyin.
- `MP3 Olarak İndir` butonuna basın.
- Alttaki durum metni ve ilerleme çubuğu, indirme ve dönüştürme sürecini gösterir.


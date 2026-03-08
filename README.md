## YouTube MP3 Converter

YouTube MP3 Converter, YouTube videolarını hızlıca **MP3 formatına dönüştürüp masaüstünüze kaydetmenizi** sağlayan basit bir masaüstü uygulamasıdır.

### Özellikler

- **Grafik arayüz**: `tkinter` ve `ttk` ile hazırlanmış sade, modern arayüz
- **YouTube → MP3 dönüştürme**: `yt-dlp` ve `ffmpeg` kullanarak en iyi ses akışını MP3'e çevirir
- **İlerleme takibi**: İlerleme çubuğu ve durum metni ile indirme/dönüştürme durumunu gösterir
- **Klasör seçimi**: Varsayılan olarak masaüstüne indirir, istenirse farklı klasör seçilebilir

### Kullanılan teknolojiler

- **Python 3**
- **tkinter / ttk** – masaüstü kullanıcı arayüzü
- **yt-dlp** – YouTube indirme ve ses ayrıştırma
- **ffmpeg** – ses dönüştürme (MP3 çıkarma)

### Kurulum

```bash
cd python/mp3_converter
python -m venv .venv
source .venv/bin/activate  # Windows için: .venv\Scripts\activate
pip install -r requirements.txt
```

`yt-dlp`, MP3 dönüştürme için sisteminizde **ffmpeg** kurulu olmasını ister:

- macOS: `brew install ffmpeg`
- Linux: `sudo apt install ffmpeg` (veya dağıtımınıza uygun komut)
- Windows: ffmpeg indirip `PATH` değişkenine ekleyin

### Çalıştırma ve kullanım

```bash
python main.py
```

- YouTube video URL'sini üstteki alana yapıştırın.
- `Klasör Seç` ile kaydedilecek klasörü seçin (varsayılan: masaüstü).
- `MP3 Olarak İndir` butonuna basın.
- İlerleme çubuğu ve durum metni, indirme ve dönüştürme sürecini gösterecektir; bittiğinde bilgilendirme penceresi çıkar.

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


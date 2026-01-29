# One Word Reel Subtitle Generator

**Create one-word reel subtitles (SRT files) that are directly importable in VN or CapCut.**

This tool uses OpenAI's Whisper model to transcribe video/audio and generates a "one-word-per-line" SRT file. It’s designed specifically for the high-energy, fast-paced subtitle style used in Instagram Reels, TikToks, and YouTube Shorts.

## 🚀 Features

* **One Word Per Segment:** Strict word-level timestamps so text pops exactly as spoken.
* **Clean Visuals:** Automatically strips commas and punctuation for a cleaner "Reel" aesthetic.
* **Optimized Performance:** Uses the Whisper `turbo` model for a perfect balance of speed and accuracy.
* **Editor Ready:** Generated `.srt` files are fully compatible with **VN Video Editor** and **CapCut**.

## 🛠️ Prerequisites

Before running the script, ensure you have **FFmpeg** installed on your system.

```bash
# macOS
brew install ffmpeg

# Ubuntu/Linux
sudo apt update && sudo apt install ffmpeg

# Windows
choco install ffmpeg

```

## 📦 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/SAGAR-TAMANG/one-word-reel-subtitle-generator.git
cd one-word-reel-subtitle-generator

```


2. **Install dependencies:**
```bash
pip install -U openai-whisper

```



## 💻 Usage

1. Open `main.py` and point the `audio_path` to your video file.
2. Run the generator:
```bash
python main.py

```


3. A file named `clean_one_word_subs.srt` will be generated in your folder.

## 📱 Importing to Editors

### For VN Video Editor:

1. Open your project in VN.
2. Tap the **Music/Text track** > **Text** > **SRT**.
3. Select the generated file.
4. Apply a global animation (like "Pop") to all segments at once for the best effect.

### For CapCut:

1. Go to **Text** > **Local Captions**.
2. Upload the `.srt` file.
3. Use the "Batch Edit" feature to style all words simultaneously.

---

## 🤝 Contributing

Feel free to open issues or submit pull requests. If you're into AI automation or local-first AI, let's connect!

**Built by [Sagar Tamang](https://github.com/SAGAR-TAMANG)**

---

### Next Step

Since you're scaling your "sagar_builds" brand, would you like me to add a **License** file (MIT) to the repo as well?
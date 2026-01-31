# 🎬 One-Word Reel Subtitle Generator

**Generate high-energy, "Hormozi-style" one-word subtitles in seconds.**

This CLI tool leverages OpenAI's Whisper (Turbo) to transcribe videos and generate `.srt` files with strict word-level timing. Perfect for creators who want that "popping" text effect in CapCut or VN without the manual grind.

## ✨ What’s New (v2.0)

* **CLI Powered:** No more hardcoding paths. Use `-i` and `-o` flags like a pro.
* **Smart Pathing:** Automatically saves SRTs in your Downloads or the source folder.
* **Model Selection:** Switch between `tiny` for speed or `large` for complex tech jargon.

## 🛠️ Installation

1. **Prerequisites:** Ensure you have [FFmpeg](https://ffmpeg.org/) installed.
2. **Clone & Install:**

```bash
git clone https://github.com/SAGAR-TAMANG/one-word-reel-subtitle-generator.git
cd one-word-reel-subtitle-generator
pip install -U openai-whisper

```

## 🚀 Usage

Run the tool directly from your terminal. By default, it uses the `turbo` model for speed.

### Basic Command

Saves the `.srt` in the same folder as your video.

```bash
python main.py -i "path/to/your/reel.mp4"

```

### Advanced Options

```bash
# Save to a specific directory (e.g., Downloads)
python main.py -i "video.mp4" -o "~/Downloads"

# Use the Large model for maximum accuracy on tech terms
python main.py -i "video.mp4" -m large

```

| Flag | Full Name | Description |
| --- | --- | --- |
| `-i` | `--input` | **Required.** Path to your video/audio file. |
| `-o` | `--output` | Directory to save the SRT (Defaults to input location). |
| `-m` | `--model` | Whisper model: `tiny`, `base`, `small`, `medium`, `large`, `turbo`. |

---

## 📱 Mobile Workflow (VN & CapCut)

1. **Generate:** Run the script on your laptop (or via **Termux** on Android).
2. **Import:** AirDrop/WhatsApp the `.srt` to your phone.
3. **VN Editor:** `Text` -> `SRT` -> `Import`.
4. **CapCut:** `Text` -> `Local Captions` -> `Upload`.
5. **Pro Tip:** Apply a "Pop" or "Spring" animation to the entire text track for that high-retention aesthetic.

---

## 🤖 For the Builders (Termux Users)

Since this tool is lightweight, you can run it locally on your Android device using Termux. Perfect for editing on the go in Bangalore traffic!

1. Install Python and FFmpeg in Termux.
2. Run the script.
3. Move the SRT to your `/sdcard/` and import directly into CapCut mobile.

---

## 🤝 Contributing

I'm building this to automate my own content workflow at **sagar_builds**. If you have ideas for auto-capitalization or color-tagging keywords, open a PR!

**Built by [Sagar Tamang**](https://github.com/SAGAR-TAMANG)
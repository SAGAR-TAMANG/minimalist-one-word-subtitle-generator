import whisper
import datetime
import re

def format_timestamp(seconds: float):
    td = datetime.timedelta(seconds=seconds)
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    secs = total_seconds % 60
    millis = int(td.microseconds / 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

def main():
    model = whisper.load_model("turbo")
    audio_path = "your-audio-or-video-path"
    
    result = model.transcribe(audio_path, word_timestamps=True)

    with open("clean_one_word_subs.srt", "w", encoding="utf-8") as f:
        counter = 1
        for segment in result["segments"]:
            for word_data in segment["words"]:
                # 1. Get the raw word
                word = word_data["word"].strip()
                
                # 2. STRIP COMMAS (and other punctuation if you like)
                word = word.replace(",", "")
                
                # Optional: Uncomment the next line to also strip periods and question marks
                # word = re.sub(r'[.,?!]', '', word)

                # Skip empty strings (in case a segment was just a comma)
                if not word:
                    continue

                start = word_data["start"]
                end = word_data["end"]

                # Write the SRT block
                f.write(f"{counter}\n")
                f.write(f"{format_timestamp(start)} --> {format_timestamp(end)}\n")
                f.write(f"{word}\n\n")
                
                counter += 1

    print("Comma-free 1-word-per-line SRT generated!")

if __name__ == "__main__":
    main()
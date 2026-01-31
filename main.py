import whisper
import datetime
import argparse
import os
from pathlib import Path

def format_timestamp(seconds: float):
    td = datetime.timedelta(seconds=seconds)
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    secs = total_seconds % 60
    millis = int(td.microseconds / 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

def process_subtitles(input_path, model_type, output_dir):
    # 1. Path Management
    video_path = Path(input_path)
    if not video_path.exists():
        print(f"Error: File {input_path} not found.")
        return

    # If no output dir is specified, save next to the video
    if output_dir:
        save_dir = Path(output_dir)
    else:
        save_dir = video_path.parent
    
    save_dir.mkdir(parents=True, exist_ok=True)
    output_filename = save_dir / f"{video_path.stem}_subs.srt"

    # 2. AI Processing
    print(f"Loading Whisper model: {model_type}...")
    model = whisper.load_model(model_type)
    
    print(f"Transcribing: {video_path.name}")
    result = model.transcribe(str(video_path), word_timestamps=True)

    # 3. Writing SRT
    with open(output_filename, "w", encoding="utf-8") as f:
        counter = 1
        for segment in result["segments"]:
            for word_data in segment["words"]:
                word = word_data["word"].strip().replace(",", "")
                
                if not word:
                    continue

                start = word_data["start"]
                end = word_data["end"]

                f.write(f"{counter}\n")
                f.write(f"{format_timestamp(start)} --> {format_timestamp(end)}\n")
                f.write(f"{word}\n\n")
                counter += 1

    print(f"✅ Success! Subtitles saved to: {output_filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate minimalist one-word SRT subtitles.")
    
    # Industry standard flags
    parser.add_argument("-i", "--input", required=True, help="Path to the input video/audio file")
    parser.add_argument("-m", "--model", default="turbo", help="Whisper model to use (tiny, base, small, medium, large, turbo)")
    parser.add_argument("-o", "--output", help="Directory to save the SRT file (defaults to video location)")

    args = parser.parse_args()

    process_subtitles(args.input, args.model, args.output)
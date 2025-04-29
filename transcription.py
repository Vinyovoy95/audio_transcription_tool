import os
import zipfile
import json
import whisper
from pathlib import Path
from pydub.utils import mediainfo
from datetime import datetime
from tqdm import tqdm

try:
    import rarfile
    rar_available = True
except ImportError:
    print("⚠️ 'rarfile' module not installed. .rar files will be ignored.")
    rar_available = False

def extract_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            try:
                if file.endswith('.zip'):
                    with zipfile.ZipFile(path, 'r') as zip_ref:
                        zip_ref.extractall(root)
                elif file.endswith('.rar') and rar_available:
                    with rarfile.RarFile(path, 'r') as rar_ref:
                        rar_ref.extractall(root)
            except Exception as e:
                print(f"[ERROR] Failed to extract {file}: {e}")

def find_audio_files(directory, extensions=None):
    if extensions is None:
        extensions = ['.mp3', '.wav', '.m4a', '.aac', '.flac', '.ogg', '.caf', '.amr', '.opus']
    audio_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                audio_files.append(Path(root) / file)
    return audio_files

def collect_metadata(audio_path):
    try:
        info = mediainfo(str(audio_path))
        duration = float(info['duration']) if 'duration' in info else 0
    except:
        duration = 0
    stat = audio_path.stat()
    return {
        "file": audio_path.name,
        "path": str(audio_path.resolve()),
        "size_MB": round(stat.st_size / (1024 * 1024), 2),
        "duration_seconds": duration,
        "modification_date": datetime.fromtimestamp(stat.st_mtime).isoformat()
    }

def transcribe_audio(model, audio_path):
    try:
        result = model.transcribe(str(audio_path))
        return result.get("text", "").strip()
    except Exception as e:
        return f"[ERROR] Transcription failed: {e}"

def main():
    base_dir = input("📂 Directory for analysis: ").strip()
    base_dir = Path(base_dir).resolve()
    if not base_dir.exists():
        print("❌ Directory not found.")
        return

    print("🔍 Extracting files...")
    extract_files(base_dir)

    print("🎧 Searching for audio files...")
    files = find_audio_files(base_dir)
    print(f"✅ {len(files)} audio files found.")

    print("🚀 Loading Whisper model...")
    model = whisper.load_model("base")  # You can use "medium" or "large" for better quality

    results = []

    for audio_path in tqdm(files, desc="📝 Transcribing"):
        metadata = collect_metadata(audio_path)
        text = transcribe_audio(model, audio_path)
        metadata["transcription"] = text
        results.append(metadata)

    output_folder = input("📁 Where to save the transcription reports? ").strip()
    output_folder = Path(output_folder).resolve()
    output_folder.mkdir(parents=True, exist_ok=True)

    file_name = f"transcription_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    output_path = output_folder / file_name

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    print(f"\n✅ Transcriptions saved in: {output_path}")

if __name__ == "__main__":
    main()

    main()

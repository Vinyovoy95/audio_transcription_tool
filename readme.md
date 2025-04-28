Audio Transcription Tool

Overview

This project provides a complete script for automatically transcribing audio files using OpenAI's Whisper model.
The code has been extensively tested and is ready for operational use.

Features

✅ Extraction of compressed files (.zip and .rar supported if the rarfile module is installed).

✅ Recursive search for audio files across folders and subfolders.

✅ Automatic audio transcription using Whisper (supports multiple formats).

✅ Metadata collection: file size, duration, modification date.

✅ Generation of a complete transcription report in .json format, combining metadata and text.

✅ Progress monitoring through a clear and responsive progress bar (tqdm).

Requirements

Python 3.12

Libraries

whisper

pydub

tqdm

rarfile (optional, for .rar extraction)

You can install the required packages via:

pip install -r requirements.txt

Usage

Clone the repository or copy the script.

Install dependencies using the provided command.

Run the script:

python script.py

Follow the on-screen prompts:

Specify the input directory (where your audio files or compressed archives are located).

Specify the output directory (where the transcription reports will be saved).

How It Works

The script first extracts any .zip and .rar archives found.

It searches for audio files across all nested folders.

For each audio file:

Metadata such as size, duration, and last modification date is collected.

The audio is transcribed using Whisper.

A structured dictionary is created with all the information.

After processing all files, a single .json file is generated containing the complete report.

Notes

If the rarfile module is not installed, .rar files will be skipped automatically (with a warning).

For higher transcription quality, you may switch the Whisper model to "medium" or "large".

Files from all supported audio extensions are processed: .mp3, .wav, .m4a, .aac, .flac, .ogg, .caf, .amr, .opus.

Example Output

Each entry in the final .json report includes:

{
    "arquivo": "example_audio.m4a",
    "caminho": "C:/Users/Example/Path/example_audio.m4a",
    "tamanho_MB": 1.25,
    "duracao_segundos": 120.5,
    "data_modificacao": "2025-04-28T15:42:30",
    "transcricao": "Hello, this is the content transcribed from the audio file."
}

Current Status

✅ Stable and operational: The script has been tested and validated.

🛠️ Extensible: Future improvements such as multi-language support and error handling enhancements can be easily incorporated.

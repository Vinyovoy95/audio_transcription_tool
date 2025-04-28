
# Audio Transcription Tool

## Overview

The **Audio Transcription Tool** is a complete solution for the automatic transcription of audio files using OpenAI’s Whisper model. Designed for operational use, the tool offers efficient processing of large audio datasets, ensuring high transcription quality, robust metadata collection, and clear output structuring.

Ideal for forensic analysts, researchers, and professionals needing reliable speech-to-text conversion across a variety of audio formats.

## Features

- **Compressed File Extraction**: Automatically extracts `.zip` and `.rar` files (requires `rarfile` module for `.rar` support).
- **Recursive Audio Search**: Detects audio files within folders and subfolders automatically.
- **Automatic Transcription**: Converts audio to text using OpenAI's Whisper model (supports multiple audio formats).
- **Metadata Collection**: Captures file size, audio duration, and last modification date.
- **Consolidated JSON Reporting**: Generates a detailed `.json` report combining metadata and transcribed text.
- **Progress Monitoring**: Real-time progress bar using `tqdm` for tracking processing status.

## Requirements

- **Python**: 3.12
- **Libraries**:
  - `whisper`
  - `pydub`
  - `tqdm`
  - `rarfile` (optional, for `.rar` extraction support)

### Install Dependencies

To install all dependencies, run the following command in your terminal:

```bash
pip install -r requirements.txt
```

This will install all the required libraries to run the Audio Transcription Tool.

## Usage

1. **Clone the repository** or copy the script to your environment.
2. **Install dependencies** by running:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the script**:

    ```bash
    python script.py
    ```

4. **Follow the prompts**:
    - Select the **input directory** (containing your audio files or compressed archives).
    - Select the **output directory** (where the JSON reports will be saved).

## How It Works

- The script first extracts any `.zip` or `.rar` archives found in the input directory.
- It then searches recursively for supported audio files in all subfolders.
- For each audio file:
  1. Metadata (size, duration, modification date) is collected.
  2. Transcription is performed using OpenAI Whisper.
  3. Data is structured into a dictionary.
  4. Finally, a single `.json` report consolidates all audio information and transcriptions.

## Notes

- If the `rarfile` library is not installed, `.rar` files will be skipped automatically (with a warning).
- To improve transcription quality, you can upgrade the Whisper model to "medium" or "large".
- Supported audio file extensions include:
  - `.mp3`, `.wav`, `.m4a`, `.aac`, `.flac`, `.ogg`, `.caf`, `.amr`, `.opus`.

## Example Output

Each entry in the generated `.json` report will have the following structure:

```json
{
  "arquivo": "example_audio.m4a",
  "caminho": "C:/Users/Example/Path/example_audio.m4a",
  "tamanho_MB": 1.25,
  "duracao_segundos": 120.5,
  "data_modificacao": "2025-04-28T15:42:30",
  "transcricao": "Hello, this is the content transcribed from the audio file."
}
```

## Current Status

- ✅ **Stable and Operational**: The script has been extensively tested.
- 🛠️ **Extensible**: Easily adaptable for future improvements such as:
  - Multilanguage transcription
  - Advanced error handling
  - Audio segmentation and speaker identification

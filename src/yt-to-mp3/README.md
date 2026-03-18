# YouTube to MP3

Download YouTube videos and convert them to MP3 audio files.

## 🌟 Features

- **Download Videos**: Fetch videos from YouTube URLs
- **Convert to MP3**: Extract audio and save as MP3
- **Batch Processing**: Process multiple videos
- **Quality Options**: Choose audio quality settings

## 🛠️ Tech Stack

- **Python** 3.10+ - Programming language
- **yt-dlp** - YouTube video downloading
- **FFmpeg** - Audio conversion

## 📁 Project Structure

```
yt-to-mp3/
├── README.md                # This file
├── yt_to_mp3.py            # Core implementation
└── __init__.py             # Module initialization
```

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- FFmpeg installed on system
- Parent project poetry environment

### Installation

From the project root:
```bash
poetry install
```

### Running YouTube to MP3

From the project root:
```bash
poetry run python src/main.py
```

Then select option "2. YouTube to MP3" from the menu.

---

## 💻 Usage

1. Select "YouTube to MP3" from the main menu
2. Enter YouTube URL(s)
3. Choose output quality
4. Wait for download and conversion to complete
5. MP3 file saved to output directory

---

## 🔧 Configuration

Create a `.env` file in the project root for custom settings:
```
OUTPUT_DIR=./downloads
AUDIO_QUALITY=192
```

---

## 📝 License

See [LICENSE](../../LICENSE) in the project root.

---

**Status**: 🚧 In Development
**Last Updated**: March 2024
# Video Converter

A powerful video to audio conversion tool that transforms video files into high-quality MP3 audio files using FFmpeg.

## 🌟 Features

- **Single Conversion**: Convert individual video files to MP3
- **Bulk Conversion**: Convert all videos in your Videos directory at once
- **Multiple Formats**: Supports MP4, MOV, MKV, and AVI video formats
- **Quality Presets**: Converts to 192k bitrate MP3 with 44100 Hz sample rate
- **User-Friendly**: Intuitive interface with clear prompts and error handling
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 🚀 Requirements

- **FFmpeg**: Required for video conversion
  - Windows: Download from [ffmpeg.org](https://ffmpeg.org/download.html)
  - macOS: `brew install ffmpeg`
  - Ubuntu/Debian: `sudo apt install ffmpeg`
  - Fedora: `sudo dnf install ffmpeg`

## 📁 Directory Structure

The converter uses standard system directories:
- **Input**: `~/Videos` - Place videos here for bulk conversion
- **Output**: `~/Music` - Converted MP3 files are saved here

## 🛠 Usage

### Single Conversion Mode
Convert individual video files:
1. Select "single" conversion mode
2. Enter the full path to your video file
3. Specify the output MP3 filename (with .mp3 extension)

### Bulk Conversion Mode
Convert all videos in your Videos directory:
1. Place all videos you want to convert in `~/Videos`
2. Select "bulk" conversion mode
3. Confirm the list of files to convert
4. All videos will be converted to MP3 in `~/Music`

## ⚙️ Technical Details

### FFmpeg Command
The converter uses this FFmpeg command structure:
```bash
ffmpeg -i input_video.mp4 -acodec libmp3lame -ab 192k -ar 44100 -y output_audio.mp3
```

### Audio Settings
- **Codec**: libmp3lame (high-quality MP3 encoder)
- **Bitrate**: 192 kbps (good balance of quality and file size)
- **Sample Rate**: 44100 Hz (CD quality)
- **Overwrite**: Automatically overwrites existing files

## 📞 Support

If you encounter issues:
1. Ensure FFmpeg is installed and accessible from your PATH
2. Verify input files exist and are readable
3. Check that you have write permissions to the Music directory

For other problems, please open an issue on the GitHub repository.
# YouTube Downloader

A simple Python wrapper for downloading YouTube videos using yt-dlp as a subprocess.

## Description

This module provides a clean interface for downloading YouTube videos in MP4 format. Unlike traditional Python wrappers that use the yt-dlp library directly, this implementation executes yt-dlp as a separate subprocess, providing better isolation and mimicking command-line usage.

## Features

- Downloads YouTube videos in highest quality MP4 format
- Uses subprocess execution for better isolation
- Automatic path creation and validation
- Comprehensive error handling with helpful messages
- Integration with the shared project structure

## Requirements

- Python 3.10+
- yt-dlp (installed via pip)

To install yt-dlp:
```bash
pip install yt-dlp
```

## Usage

The YouTube downloader can be used through the main application:

```bash
python -m py_scripts_for_life.youtube_downloader.app
```

Or imported and used programmatically:

```python
from py_scripts_for_life.youtube_downloader.downloader import YouTubeDownloader

downloader = YouTubeDownloader(
    url="https://www.youtube.com/watch?v=example",
    save_path="/path/to/save/videos"
)
downloader.yt_downloader()
```

## How It Works

Instead of using the yt-dlp Python library directly, this implementation:

1. Constructs yt-dlp command-line arguments
2. Executes yt-dlp as a subprocess
3. Handles stdout/stderr appropriately
4. Provides meaningful error messages

This approach offers several advantages:
- Better isolation from the main Python process
- More closely mimics manual command-line usage
- Easier troubleshooting and debugging
- Consistent behavior with the video_converter module

## Error Handling

The downloader handles various error conditions:

- Missing yt-dlp installation
- Network connectivity issues
- Invalid URLs or geo-restricted content
- Permission errors when saving files

All errors provide actionable feedback to help resolve the issue.

## Integration

This module follows the same patterns as other scripts in the py-scripts-for-life project:

- Uses shared constants for file paths
- Implements consistent error handling
- Follows project coding standards
- Integrates with the main application structure
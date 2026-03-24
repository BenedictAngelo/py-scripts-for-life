#!/usr/bin/env python3
"""
Test script for the YouTube downloader functionality.
"""

import sys
from pathlib import Path

from src.py_scripts_for_life.youtube_downloader.downloader import YouTubeDownloader


def test_youtube_downloader():
    """Test the YouTube downloader with a simple URL."""
    # Use a simple test URL (you can replace this with an actual video)
    test_url = "https://www.youtube.com/watch?v=jNQXAC9IVRw"  # First YouTube video

    # Use a temporary directory for testing
    test_path = str(Path.home() / "Videos" / "test_downloads")

    print(f"Testing YouTube downloader...")
    print(f"URL: {test_url}")
    print(f"Save path: {test_path}")

    try:
        downloader = YouTubeDownloader(url=test_url, save_path=test_path)
        downloader.yt_downloader()
        print("Download test completed successfully!")
        return True
    except Exception as e:
        print(f"Error during download test: {e}")
        return False


if __name__ == "__main__":
    print("Running YouTube downloader test...")
    success = test_youtube_downloader()
    sys.exit(0 if success else 1)

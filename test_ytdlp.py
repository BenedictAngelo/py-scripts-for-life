#!/usr/bin/env python3
"""
Test script to check if yt-dlp is available in the current environment.
"""

import subprocess
import sys


def test_yt_dlp():
    """Test if yt-dlp is available and working."""
    try:
        # Try to run yt-dlp with --version flag
        result = subprocess.run(
            ["yt-dlp", "--version"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        print("yt-dlp is available!")
        print(f"Version: {result.stdout.strip()}")
        return True
    except FileNotFoundError:
        print("Error: yt-dlp not found. Please install yt-dlp.")
        print("You can install it with: pip install yt-dlp")
        return False
    except subprocess.CalledProcessError as e:
        print(f"Error running yt-dlp: {e}")
        print(f"stderr: {e.stderr}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False


if __name__ == "__main__":
    print("Testing yt-dlp availability...")
    success = test_yt_dlp()
    sys.exit(0 if success else 1)

#!/usr/bin/env python3
"""
Simple test script to verify subprocess functionality for YouTube downloader.
"""

import subprocess
import sys
from pathlib import Path


def test_subprocess_yt_dlp():
    """Test subprocess execution of yt-dlp with a simple command."""
    print("Testing subprocess execution of yt-dlp...")

    # Simple test command - just get version info
    cmd = ["yt-dlp", "--version"]

    try:
        result = subprocess.run(
            cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        print("SUCCESS: yt-dlp subprocess execution works!")
        print(f"Version: {result.stdout.strip()}")
        return True
    except FileNotFoundError:
        print("ERROR: yt-dlp not found in PATH")
        return False
    except subprocess.CalledProcessError as e:
        print(f"ERROR: Command failed with return code {e.returncode}")
        print(f"stderr: {e.stderr}")
        return False
    except Exception as e:
        print(f"ERROR: Unexpected exception: {e}")
        return False


def test_help_command():
    """Test subprocess execution with help command."""
    print("\nTesting help command...")

    cmd = ["yt-dlp", "--help"]

    try:
        result = subprocess.run(
            cmd,
            check=True,
            stdout=subprocess.DEVNULL,  # Suppress output for help
            stderr=subprocess.PIPE,
        )
        print("SUCCESS: Help command works!")
        return True
    except Exception as e:
        print(f"ERROR: Help command failed: {e}")
        return False


if __name__ == "__main__":
    print("Running subprocess tests for YouTube downloader...\n")

    success1 = test_subprocess_yt_dlp()
    success2 = test_help_command()

    if success1 and success2:
        print("\nAll tests passed! The subprocess implementation is working correctly.")
        sys.exit(0)
    else:
        print("\nSome tests failed. Check the error messages above.")
        sys.exit(1)

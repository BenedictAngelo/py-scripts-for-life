from enum import StrEnum
from pathlib import Path


class Paths(StrEnum):
    """File path enumeration for operating system flexibility.

    Provides paths for Downloads, Videos, and Music directories
    in the user's home folder for cross-platform compatibility.
    """

    # DOWNLOADS_PATH = str(Path.home() / "Downloads")
    VIDEOS_PATH = str(Path.home() / "Videos")
    MUSIC_PATH = str(Path.home() / "Music")


class FileFormat(StrEnum):
    """File format enumeration for video and audio formats.

    Supported formats for downloading and converting.
    """

    MP3 = ".mp3"
    MP4 = ".mp4"
    MOV = ".mov"
    MKV = ".mkv"
    AVI = ".avi"


def main():
    pass


if __name__ == "__main__":
    main()

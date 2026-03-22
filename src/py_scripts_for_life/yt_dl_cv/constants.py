from enum import Enum, StrEnum
from pathlib import Path


class Paths(Enum):
    """File path enumeration for operating system flexibility.

    Provides paths for Downloads, Videos, and Music directories
    in the user's home folder for cross-platform compatibility.
    """

    DOWNLOADS_PATH = Path.home() / "Downloads"
    VIDEOS_PATH = Path.home() / "Videos"
    MUSIC_PATH = Path.home() / "Music"


class Has_The_Files(Enum):
    """File existence check enumeration.

    Used to validate if a directory contains files with required formats.
    YES = True (files exist), NO = False (files don't exist)
    """

    YES = True
    NO = False


class Genre(StrEnum):
    """Genre enumeration for metadata tagging.

    Contains different types of genres for video/audio metadata.
    Used when converting or downloading media files.
    """

    GAME = "Video Game"
    MUSIC = "Music"
    SPORT = "Sport"
    STUDY = "Study"
    PODCAST = "Podcast"
    DOCUMENTARY = "Documentary"
    COMEDY = "Comedy"
    TUTORIAL = "Tutorial"
    NEWS = "News"
    ENTERTAINMENT = "Entertainment"
    OTHER = "Other"


class FileFormat(StrEnum):
    """File format enumeration for video and audio formats.

    Supported formats for downloading and converting.
    """

    MP4 = ".mp4"
    MP3 = ".mp3"
    MOV = ".mov"
    MKV = ".mkv"
    AVI = ".avi"


def main():
    pass


if __name__ == "__main__":
    main()

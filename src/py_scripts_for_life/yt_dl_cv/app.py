from dataclasses import dataclass
from enum import Enum, StrEnum
from pathlib import Path


class Paths(Enum):
    """File path enumeration for operating system flexibility, currently only holds for Downloads, Videos, Music"""

    DOWNLOADS_PATH = Path.home() / "Downloads"
    VIDEOS_PATH = Path.home() / "Videos"
    MUSIC_PATH = Path.home() / "Musics"


class Has_The_Files(Enum):
    """File enumeration that can be used if directory has the file needed or not, yes is true, no is false"""

    YES = True
    NO = False


class Genre(StrEnum):
    """Genre enumeration, containing different types of
    genre for metadata of videos"""

    GAME = "Video Game"
    MUSIC = "Music"
    SPORT = "Sport"
    STUDY = "Study"


class FileFormat(StrEnum):
    """File format enumeration for video and audio formats"""

    MP4 = ".mp4"
    MP3 = ".mp3"
    MOV = ".mov"


@dataclass
class Downloader:
    url: str
    destination: Paths


@dataclass
class Converter:
    input_file: str
    output_file: str


@dataclass
class MetaData:
    title: str
    author: str
    genre: Genre


def app() -> None:
    """Main application loop for YouTube Downloader."""
    pass


def main() -> None:
    """Entry point for YouTube Downloader application."""
    app()


if __name__ == "__main__":
    main()

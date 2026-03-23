from ..shared import Graphics
from .constants import Paths
from .mode import ConversionPrompts


def app() -> None:
    """Main application loop for Video converter."""
    title: str = "Video converter"
    Graphics.script_title(title)
    while True:
        reply: str = input(
            "Choose convert mode 'single' conversion or 'bulk' conversion (q to quit): "
        )
        match reply.lower():
            case "single" | "":
                print("\n**You chose 'single' conversion\n")
                ConversionPrompts().single_convert()
            case "bulk":
                print("\n**You chose 'bulk' conversion\n")
                print(
                    f"\n**Bulk convert automatically converts every video format (.mp4, .mov, .mkv, .avi) in your '{Paths.VIDEOS_PATH}'\ninto '.mp3' format to your '{Paths.MUSIC_PATH}'**\n"
                )
                prompt: str = input(
                    "Are you sure you want you want to proceed? (y/n) (q to quit)"
                )
                match prompt.lower():
                    case "y" | "":
                        ConversionPrompts().bulk_convert()
                    case "n":
                        continue
                    case "q":
                        Graphics.closing()
                        exit()
                    case _:
                        print("\nInvalid input, try again\n")


def main() -> None:
    app()
    """Entry point for YouTube Downloader application."""


if __name__ == "__main__":
    main()

"""Main application entry point for the Video Converter."""

from ..shared import Graphics
from ..shared.authenticators import Authenticators
from .constants import Paths
from .mode import ConversionPrompts


def app() -> None:
    """Main application loop for Video converter."""
    title: str = "Video Converter"
    Graphics.script_title(title)

    # Display instructions
    print("Single mode: Convert individual video files to MP3")
    print(
        f"Bulk mode: Convert all videos in '{Paths.VIDEOS_PATH}' to MP3 files in '{Paths.MUSIC_PATH}'"
    )
    print("")

    while True:
        reply: str = Authenticators.get_user_input(
            "Choose convert mode 'single' conversion or 'bulk' conversion (q to quit): ",
            allow_quit=True,
        )

        match reply.lower():
            case "single" | "":
                print("\n**You chose 'single' conversion**\n")
                ConversionPrompts().single_convert()
            case "bulk":
                print("\n**You chose 'bulk' conversion**\n")
                print(
                    f"\n**Bulk convert automatically converts every video format (.mp4, .mov, .mkv, .avi) in your '{Paths.VIDEOS_PATH}'\ninto '.mp3' format to your '{Paths.MUSIC_PATH}'**\n"
                )
                ConversionPrompts().bulk_convert()
            case _:
                print("\nInvalid input, try again\n")


def main() -> None:
    """Entry point for Video Converter application."""
    app()


if __name__ == "__main__":
    main()

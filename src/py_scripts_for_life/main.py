"""
Main entry point for Py Scripts for Life.
Displays menu of available tools and routes user selection.
"""

from .yt_dl_cv import app as yt_downloader_vid_converter
from .password_manager import app as password_manager
from .shared import Graphics


def menu() -> None:
    """Display main menu and handle tool selection."""
    try:
        choices = [
            [1, "YouTube Downloader (MP4) & Video Converter (MP4 to MP3)"],
            [2, "Password Manager"],
            [3, "Future Project 3"],
        ]

        Graphics.main_title()

        while True:
            for num, tool_name in choices:
                print(" " * 20 + f"{num}. {tool_name}")
            print("\n" + " " * 20 + "q. Quit")

            choice: str = input(
                "\nWhat tool do you want to use? (1-3) (q to quit): "
            ).lower()

            match choice:
                case "q":
                    Graphics.closing()
                    exit()
                case "1":
                    yt_downloader_vid_converter()
                case "2":
                    password_manager()
                case "3":
                    print("\nFuture Project 3 - Coming soon!\n")
                case _:
                    print("\nInvalid input. Please enter a valid option (1-3 or q).\n")
                    continue
    except KeyboardInterrupt:
        Graphics.closing()
    finally:
        exit()


def main() -> None:
    """Entry point for the application."""
    menu()


if __name__ == "__main__":
    main()

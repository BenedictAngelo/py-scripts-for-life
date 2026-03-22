"""
Main entry point for Py Scripts for Life.
Displays menu of available tools and routes user selection.
"""

from .password_manager import app as password_manager
from .shared import Graphics
from .video_converter import app as video_converter


def menu() -> None:
    """Display main menu and handle tool selection."""
    try:
        choices = [
            [1, "YouTube donwloader"],
            [2, "Video Converter"],
            [3, "Password Manager"],
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
                    print("\nYoutube to MP4 downlaoder!\n")
                case "2":
                    video_converter()
                case "3":
                    password_manager()
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

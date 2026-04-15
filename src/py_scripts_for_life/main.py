"""
Main entry point for Py Scripts for Life.
Displays menu of available tools and routes user selection.
"""

from .lib import menu


def main() -> None:
    """Entry point for the application."""
    menu()


if __name__ == "__main__":
    main()

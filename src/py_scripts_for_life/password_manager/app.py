"""
Password Manager application entry point.
Provides CLI menu for managing passwords with add, view, and delete modes.
"""

from ..shared import Graphics
from .modes import PasswordMode


def app() -> None:
    """Main application loop for Password Manager."""
    title: str = "Password Manager"
    Graphics.script_title(title)

    while True:
        choice: str = input(
            "\nChoose what mode do you want:\n"
            "  (a)dd    - Add new password\n"
            "  (v)iew   - View all passwords\n"
            "  (d)elete - Delete password\n"
            "  (q)uit   - Quit\n"
            "\nYour choice: "
        )
        PasswordMode(choice).mode()


def main() -> None:
    """Entry point for the password manager."""
    app()


if __name__ == "__main__":
    main()

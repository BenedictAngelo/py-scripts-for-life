from ..shared import Graphics
from .modes import PasswordMode


def app() -> None:
    """Main application loop for Password Manager."""
    title: str = "Password Manager"
    Graphics.script_title(title)

    while True:
        choice: str = input(
            "Choose what mode do you want, 'add' or 'view'? (q to quit): "
        )
        PasswordMode(choice).mode()


def main() -> None:
    app()


if __name__ == "__main__":
    main()

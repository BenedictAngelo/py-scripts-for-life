"""
Shared UI graphics and formatting utilities.

Provides consistent visual formatting for all scripts including
titles, borders, and decorative elements.
"""


class Graphics:
    """Class and and collection of graphical printing for looks and designing the apps"""

    @staticmethod
    def main_title() -> tuple:
        """Display the main application title banner."""
        title_display: tuple[None, None, None, None, None] = (
            print(
                "*******************************************************************"
            ),
            print(
                "|==============|   Py Scripts for every day life   |==============|"
            ),
            print(
                "|===================|   by: Benedict Angelo   |===================|"
            ),
            print(
                "*******************************************************************"
            ),
            print(""),
        )
        return title_display

    @staticmethod
    def closing() -> tuple:
        """Display the program closing/exit banner."""
        closing_display: tuple[None, None, None, None] = (
            print("\n\nExiting...\n"),
            print(
                "*******************************************************************"
            ),
            print(
                "|=====================|   Program Closed.   |=====================|"
            ),
            print(
                "*******************************************************************"
            ),
        )
        return closing_display

    @staticmethod
    def read_border() -> None:
        """Print a horizontal border line."""
        border: None = print(
            "==================================================================="
        )
        return border

    @staticmethod
    def data_border() -> None:
        """Print a data separator line."""
        border: None = print(
            "-------------------------------------------------------------------"
        )
        return border

    @staticmethod
    def script_title(title) -> tuple:
        """
        Display a script/module title with borders.

        Args:
            title: Name of the script/module being executed
        """
        script_title: tuple[None, None, None, None, None] = (
            print(""),
            Graphics.read_border(),
            print(f"You chose '{title}':"),
            Graphics.read_border(),
            print(""),
        )
        return script_title

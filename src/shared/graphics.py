"""
Shared UI graphics and formatting utilities.

Provides consistent visual formatting for all scripts including
titles, borders, and decorative elements.
"""


def main_title():
    """Display the main application title banner."""
    print("*******************************************************************")
    print("|==============|   Py Scripts for every day life   |==============|")
    print("|===================|   by: Benedict Angelo   |===================|")
    print("*******************************************************************")
    print("")


def closing():
    """Display the program closing/exit banner."""
    print("")
    print("*******************************************************************")
    print("|=====================|   Program Closed.   |=====================|")
    print("*******************************************************************")


def read_border():
    """Print a horizontal border line."""
    print("===================================================================")


def data_border():
    """Print a data separator line."""
    print("-------------------------------------------------------------------")


def script_title(title):
    """
    Display a script/module title with borders.

    Args:
        title: Name of the script/module being executed
    """
    print("")
    read_border()
    print(f"You chose '{title}':")
    read_border()
    print("")

"""
Main entry point for Py Scripts for Life.
Displays menu of available tools and routes user selection.
"""

from password_manager import app as password_manager
from shared import closing, main_title


def menu():
    """Display main menu and handle tool selection."""
    choices = [
        [1, "Password Manager"],
        [2, "Future Project 2"],
        [3, "Future Project 3"],
    ]

    main_title()

    while True:
        for num, tool_name in choices:
            print(" " * 20 + f"{num}. {tool_name}")
        print(" " * 20 + "q. Quit")

        choice = input("\nWhat tool do you want to use? (1-3) (q to quit): ").lower()

        match choice:
            case "q":
                print("Exiting...")
                closing()
                exit()
            case "1":
                password_manager()
            case "2":
                print("Future Project 2 - Coming soon!")
            case "3":
                print("Future Project 3 - Coming soon!")
            case _:
                print("Invalid input. Please enter a valid option (1-3 or q).")
                continue


def main():
    """Entry point for the application."""
    menu()


if __name__ == "__main__":
    main()

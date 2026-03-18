"""
Main entry point for Py Scripts for Life.
Displays menu of available tools and routes user selection.
"""

from password_manager import app as password_manager
from shared import closing, main_title


def menu():
    """
    Display main menu and handle tool selection.
    Routes user choice to appropriate application.
    """
    # Define available tools with their numbers and names
    choices = [
        [1, "Password Manager"],
        [2, "Future Project 2"],
        [3, "Future Project 3"],
    ]

    # Display main title banner
    main_title()

    while True:
        # Display menu options
        for num, tool_name in choices:
            print(" " * 20 + f"{num}. {tool_name}")
        print(" " * 20 + "q. Quit")

        # Get user choice
        choice = input("\nWhat tool do you want to use? (1-3) (q to quit): ").lower()

        # Route to selected tool or handle exit
        match choice:
            case "q":
                print("Exiting...")
                closing()
                exit()
            case "1":
                # Launch Password Manager
                password_manager()
            case "2":
                # Placeholder for future project 2
                print("Future Project 2 - Coming soon!")
            case "3":
                # Placeholder for future project 3
                print("Future Project 3 - Coming soon!")
            case _:
                # Handle invalid input
                print("Invalid input. Please enter a valid option (1-3 or q).")
                continue


def main():
    """Entry point for the application."""
    menu()


if __name__ == "__main__":
    main()

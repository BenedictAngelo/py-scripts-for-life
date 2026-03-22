"""
Shared authenticators module for input validation across all scripts.

Provides reusable functions for user interaction including:
- User input with optional quit capability ('q')
- Yes/No prompts with validation
"""

from typing import Callable, Optional

from .graphics import Graphics


class Authenticators:
    """
    Collection of reusable input validation functions for user interaction.

    Supports:
    - get_user_input() - Get input with optional quit capability ('q')
    - get_yes_no_input() - Get yes/no confirmation with validation

    All methods support graceful exit with 'q' input (can be disabled).
    """

    @staticmethod
    def get_user_input(
        prompt: str,
        validation_func: Optional[Callable[[str], bool]] = None,
        allow_quit: bool = True,
    ) -> str:
        """
        Get user input with optional validation and quit capability.

        Args:
            prompt: Input prompt message displayed to user
            validation_func: Optional function to validate input.
                           Should return True if valid, False otherwise.
            allow_quit: Allow user to quit with 'q' input (default: True).
                       If True, 'q' triggers graceful exit.

        Returns:
            Valid user input as string

        Raises:
            SystemExit: If user enters 'q' and allow_quit is True

        Examples:
            # Basic input
            website = Authenticators.get_user_input("Enter website: ")

            # Input without quit option
            website = Authenticators.get_user_input(
                "Enter website: ",
                allow_quit=False
            )

            # Input with validation (must be digits)
            length = Authenticators.get_user_input(
                "Enter password length: ",
                validation_func=lambda x: x.isdigit(),
                allow_quit=True
            )
        """
        while True:
            # Lowercase input only for y/n prompts, preserve case otherwise
            user_input = input(prompt).lower() if "y/n" in prompt else input(prompt)

            # Check for quit request
            if allow_quit and user_input.lower() == "q":
                Graphics.closing()
                exit()

            # Validate input if validation function provided
            if validation_func and not validation_func(user_input):
                continue

            return user_input

    @staticmethod
    def get_yes_no_input(prompt: str, allow_quit: bool = True) -> bool:
        """
        Get yes/no confirmation input with validation.

        Args:
            prompt: Question to ask user
            allow_quit: Allow user to quit with 'q' input (default: True).
                       If True, 'q' triggers graceful exit.

        Returns:
            True if user enters 'y', 'yes', or empty string (default)
            False if user enters 'n' or 'no'

        Raises:
            SystemExit: If user enters 'q' and allow_quit is True

        Examples:
            # Basic yes/no confirmation
            confirm = Authenticators.get_yes_no_input("Are you sure? (y/n): ")

            # Without quit option
            confirm = Authenticators.get_yes_no_input(
                "Continue? (y/n): ",
                allow_quit=False
            )
        """
        while True:
            response: str = Authenticators.get_user_input(
                prompt, allow_quit=allow_quit
            ).lower()

            if response in ("y", "yes", ""):
                return True
            elif response in ("n", "no"):
                return False
            else:
                print("\nInvalid input. Please enter 'y' or 'n'.\n")
                continue

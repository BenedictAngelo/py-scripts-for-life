from cryptography.fernet import Fernet

from shared import Graphics

from .password_generator import PasswordManager


class PasswordMode:
    """
    Handles different modes: 'view' existing passwords or 'add' new ones.
    """

    file_path: str = "outputs/passwords.txt"

    def __init__(self, choice: str):
        """Initialize mode handler."""
        self.choice = choice

    @staticmethod
    def view(fer: Fernet = PasswordManager.encryptor()) -> None:
        """
        Display all stored passwords from passwords.txt file.
        Decrypts passwords for display using the key.key cipher.
        """
        try:
            Graphics.read_border()
            with open(PasswordMode.file_path, "r") as f:
                for line in f.readlines():
                    if line.strip():
                        data = line.rstrip()
                        website_view, email_view, pwd_view, time_view = data.split("|")

                        print("")
                        Graphics.data_border()
                        print(f"Website: {website_view}")
                        print(f"Email: {email_view}")
                        print(f"Password: {fer.decrypt(pwd_view.encode()).decode()}")
                        print(f"Time created: {time_view}")
                        Graphics.data_border()
                        print("")
            Graphics.read_border()
        except FileNotFoundError:
            Graphics.read_border()
            print("\nNo 'passwords.txt' file was found.")
            print("Creating file...")
            with open(PasswordMode.file_path, "a") as f:
                f.write("")
            print(
                "\nFile successfully created in 'outputs/' directory but empty for now\n"
            )
        finally:
            pass

    @staticmethod
    def _get_user_input(
        prompt: str, validation_func: None = None, allow_quit: bool = True
    ) -> str:
        """
        Reusable input validation function to reduce code redundancy.

        Args:
            prompt: Input prompt message
            validation_func: Optional function to validate input (returns True if valid)
            allow_quit: Allow user to quit with 'q' input

        Returns:
            Valid user input
        """
        while True:
            user_input = input(prompt).lower() if "y/n" in prompt else input(prompt)

            if allow_quit and user_input.lower() == "q":
                Graphics.closing()
                exit()

            if validation_func and not validation_func(user_input):
                continue

            return user_input

    @staticmethod
    def _get_yes_no_input(prompt: str) -> bool:
        """
        Get yes/no input with validation.

        Args:
            prompt: Question to ask user

        Returns:
            True if 'y', False if 'n'
        """
        while True:
            response: str = PasswordMode._get_user_input(prompt).lower()
            if response == "y" or "yes" or "":
                return True
            elif response == "n" or "no":
                return False
            else:
                print("\nInvalid input. Please enter 'y' or 'n'.")
                continue
        return response

    @staticmethod
    def add() -> None:
        """
        Interactive mode to add a new password entry.
        Prompts user for website, email, and password preferences.
        Generates password and saves to passwords.txt.
        """
        while True:
            website: str = PasswordMode._get_user_input(
                "\nFor what website will you use it? (q to quit): "
            )
            email: str = PasswordMode._get_user_input(
                "\nWhat email will you use it for? (q to quit): "
            )

            max_character_str: str = PasswordMode._get_user_input(
                "\nHow many maximum characters in password do you want? (digits only or q to quit): "
            )
            if not max_character_str.isdigit():
                print("\nInvalid input. Please enter digits only.")
                continue
            max_character: int = int(max_character_str)

            numbers: bool = PasswordMode._get_yes_no_input(
                "\nDo you want digits in your password? (y/n) (q to quit): "
            )
            special_characters: bool = PasswordMode._get_yes_no_input(
                "\nDo you want special characters in your password? (y/n) (q to quit): "
            )

            password_mgr = PasswordManager(
                website, email, max_character, numbers, special_characters
            )

            data_line = "|".join(
                [
                    password_mgr.what_website(),
                    password_mgr.what_email(),
                    password_mgr.what_password(),
                    password_mgr.what_time(),
                ]
            )

            with open(PasswordMode.file_path, "a") as f:
                f.write(data_line + "\n")
            print(
                "\nPassword successfully written! See 'outputs/passwords.txt' or in 'view' mode.\n"
            )
            break

    def mode(self):
        """Route user choice to appropriate mode handler."""
        match self.choice.lower():
            case "view":
                PasswordMode.view()
            case "add":
                PasswordMode.add()
            case "q":
                Graphics.closing()
                exit()
            case _:
                print("Invalid input. Please choose 'add', 'view', or 'q'.")

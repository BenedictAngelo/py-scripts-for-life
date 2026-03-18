import datetime
import random
import string

from cryptography.fernet import Fernet

from shared import closing, read_border, script_title


class PasswordGenerator:
    """
    Generates secure random passwords with customizable criteria.

    Supports:
    - Custom password length
    - Optional digit inclusion
    - Optional special character inclusion
    - Automatic encryption of generated passwords
    """

    def __init__(
        self, max_character: int, numbers: bool = True, special_characters: bool = True
    ):
        """
        Initialize the password generator.

        Args:
            max_character: Minimum length of the password
            numbers: Include digits in password (default: True)
            special_characters: Include special characters (default: True)
        """
        self.max_character = max_character
        self.numbers = numbers
        self.special_characters = special_characters

    @staticmethod
    def encryptor():
        """
        Load encryption cipher from key.key file.

        Returns:
            Fernet cipher object for encryption/decryption
        """
        with open("key.key", "rb") as key_file:
            key = key_file.read()
        return Fernet(key)

    def generator(self):
        """
        Generate a random password meeting the specified criteria.

        Returns:
            Encrypted password string
        """
        fer = PasswordGenerator.encryptor()

        letters = string.ascii_letters
        digits = string.digits
        specials = string.punctuation

        characters = letters
        if self.numbers:
            characters += digits
        if self.special_characters:
            characters += specials

        password = ""
        meets_criteria = False
        has_number = False
        has_special = False

        while not meets_criteria or len(password) < self.max_character:
            new_char = random.choice(characters)
            password += new_char

            if new_char in digits:
                has_number = True
            elif new_char in specials:
                has_special = True

            meets_criteria = True
            if self.numbers:
                meets_criteria = has_number
            if self.special_characters:
                meets_criteria = meets_criteria and has_special

        encrypted_password = fer.encrypt(password.encode()).decode()
        return encrypted_password


class PasswordManager(PasswordGenerator):
    """
    Manages password storage with website, email, and metadata.
    Inherits password generation capabilities from PasswordGenerator.
    """

    def __init__(
        self,
        website: str,
        email: str,
        max_character: int,
        numbers: bool = True,
        special_characters: bool = True,
    ):
        """
        Initialize password manager with user credentials and generation settings.

        Args:
            website: Website/service name
            email: Email address associated with password
            max_character: Password length
            numbers: Include digits
            special_characters: Include special characters
        """
        super().__init__(max_character, numbers, special_characters)
        self.website = website
        self.email = email
        self.password = self.generator()
        self.time_now = datetime.datetime.now().strftime("%I:%M:%S %a %b-%d-%Y")

    def what_website(self) -> str:
        """Return the website/service name."""
        return self.website

    def what_email(self) -> str:
        """Return the email address."""
        return self.email

    def what_password(self) -> str:
        """Return the encrypted password."""
        return self.password

    def what_time(self) -> str:
        """Return the time when password was created."""
        return self.time_now


class PasswordMode:
    """
    Handles different modes: 'view' existing passwords or 'add' new ones.
    """

    def __init__(self, choice: str):
        """Initialize mode handler."""
        self.choice = choice

    @staticmethod
    def view():
        """
        Display all stored passwords from passwords.txt file.
        Decrypts passwords for display using the key.key cipher.
        """
        fer = PasswordGenerator.encryptor()
        try:
            read_border()
            with open("passwords.txt", "r") as f:
                for line in f.readlines():
                    if line.strip():
                        data = line.rstrip()
                        website_view, email_view, pwd_view, time_view = data.split("|")

                        print(f"\nWebsite: {website_view}")
                        print(f"Email: {email_view}")
                        print(f"Password: {fer.decrypt(pwd_view.encode()).decode()}")
                        print(f"Time created: {time_view}")
                        print("-" * 67)
            read_border()
        except FileNotFoundError:
            read_border()
            print("\nNo 'passwords.txt' file was found.")
            print("Creating file...")
            with open("passwords.txt", "a") as f:
                f.write("")
            print("\nFile successfully created but empty for now\n")

    @staticmethod
    def _get_user_input(
        prompt: str, validation_func=None, allow_quit: bool = True
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
                print("Exiting...")
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
            response = PasswordMode._get_user_input(prompt).lower()
            match response:
                case "y":
                    return True
                case "n":
                    return False
                case _:
                    print("\nInvalid input. Please enter 'y' or 'n'.")

    @staticmethod
    def add():
        """
        Interactive mode to add a new password entry.
        Prompts user for website, email, and password preferences.
        Generates password and saves to passwords.txt.
        """
        while True:
            website = PasswordMode._get_user_input(
                "\nFor what website will you use it? (q to quit): "
            )
            email = PasswordMode._get_user_input(
                "\nWhat email will you use it for? (q to quit): "
            )

            max_character_str = PasswordMode._get_user_input(
                "\nHow many maximum characters in password do you want? (digits only or q to quit): "
            )
            if not max_character_str.isdigit():
                print("\nInvalid input. Please enter digits only.")
                continue
            max_character = int(max_character_str)

            numbers = PasswordMode._get_yes_no_input(
                "\nDo you want digits in your password? (y/n) (q to quit): "
            )
            special_characters = PasswordMode._get_yes_no_input(
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

            with open("passwords.txt", "a") as f:
                f.write(data_line + "\n")
            print("\nPassword successfully written!\n")
            break

    def mode(self):
        """Route user choice to appropriate mode handler."""
        match self.choice.lower():
            case "view":
                PasswordMode.view()
            case "add":
                PasswordMode.add()
            case "q":
                print("Exiting...")
                closing()
                exit()
            case _:
                print("Invalid input. Please choose 'add', 'view', or 'q'.")


def app():
    """Main application loop for Password Manager."""
    title = "Password Manager"
    script_title(title)

    try:
        while True:
            choice = input(
                "Choose what mode do you want, 'add' or 'view'? (q to quit): "
            )
            PasswordMode(choice).mode()
    except KeyboardInterrupt:
        print("\n\nProgram has been forcefully canceled.\n")
    finally:
        closing()
        exit()


def main():
    """Entry point for the password manager application."""
    app()


if __name__ == "__main__":
    main()

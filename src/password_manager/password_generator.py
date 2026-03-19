import datetime
import random
import string

from cryptography.fernet import Fernet


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
    def encryptor() -> Fernet:
        """
        Load encryption cipher from key.key file.

        Returns:
            Fernet cipher object for encryption/decryption
        """
        try:
            with open("outputs/key.key", "rb") as key_file:
                key: bytes = key_file.read()
        except FileNotFoundError:
            print("Key does not exist, creating...")
            key = Fernet.generate_key()
            with open("outputs/key.key", "wb") as key_file:
                key_file.write(key)

        return Fernet(key)

    def generator(self) -> str:
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

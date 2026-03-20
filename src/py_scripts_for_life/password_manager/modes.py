"""
Password Manager modes: view, add, and delete operations.
Uses SQLite database for persistent storage.
"""

from cryptography.fernet import Fernet

from ..shared import Graphics
from .database import PasswordDatabase
from .password_generator import PasswordManager


class PasswordMode:
    """
    Handles different modes: 'view', 'add', and 'delete' password entries.
    Uses SQLite database instead of file-based storage.
    Each password entry has a unique ID for easy identification.

    Supported modes:
    - 'a' or 'add': Add new password
    - 'v' or 'view': View all passwords
    - 'd' or 'delete': Delete password
    - 'q' or 'quit': Exit application
    """

    def __init__(self, choice: str):
        """Initialize mode handler."""
        self.choice = choice
        self.db = PasswordDatabase()

    @staticmethod
    def _get_user_input(
        prompt: str, validation_func=None, allow_quit: bool = True
    ) -> str:
        """
        Reusable input validation function to reduce code redundancy.

        Args:
            prompt: Input prompt message
            validation_func: Optional function to validate input
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
            if response in ("y", "yes", ""):
                return True
            elif response in ("n", "no"):
                return False
            else:
                print("\nInvalid input. Please enter 'y' or 'n'.\n")
                continue

    def view(self) -> None:
        """
        Display all stored passwords from database.
        Shows ID, website, email, decrypted password, and creation date.
        """
        passwords = self.db.get_all_passwords()

        if not passwords:
            Graphics.read_border()
            print("\nNo passwords found in database.\n")
            Graphics.read_border()
            return

        fer = PasswordManager.encryptor()
        Graphics.read_border()
        print(f"\nTotal passwords: {len(passwords)}\n")

        for password_entry in passwords:
            password_id, website, email, encrypted_password, created_at = password_entry

            print("")
            Graphics.data_border()
            print(f"ID: {password_id}")
            print(f"Website: {website}")
            print(f"Email: {email}")
            print(f"Password: {fer.decrypt(encrypted_password.encode()).decode()}")
            print(f"Created: {created_at}")
            Graphics.data_border()
            print("")

        Graphics.read_border()

    def add(self) -> None:
        """
        Interactive mode to add a new password entry.
        Generates password and saves to database with auto-generated unique ID.

        Password length defaults to 18 if user presses Enter without input.
        Website and email have no defaults - user must provide them.
        """
        while True:
            website: str = PasswordMode._get_user_input(
                "\nFor what website will you use it? (q to quit): "
            )
            email: str = PasswordMode._get_user_input(
                "\nWhat email will you use it for? (q to quit): "
            )

            # Get password length with default of 18
            max_character_str: str = input(
                "\nHow many maximum characters in password do you want? (Empty for default:'18', or q to quit): "
            )

            if max_character_str.lower() == "q":
                Graphics.closing()
                exit()

            # Default to 18 if empty string
            if max_character_str == "":
                max_character = 18
                print("Using default password length: 18 characters")
            else:
                if not max_character_str.isdigit():
                    print("\nInvalid input. Please enter digits only.\n")
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

            password_id = self.db.add_password(
                password_mgr.what_website(),
                password_mgr.what_email(),
                password_mgr.what_password(),
                password_mgr.what_time(),
            )

            if password_id > 0:
                print(f"\n✅ Password successfully saved with ID: {password_id}\n")
            else:
                print("\n❌ Error saving password. Please try again.\n")

            break

    def delete(self) -> None:
        """
        Interactive mode to delete password entries.
        Allows deletion by ID or deletion of all passwords.
        Requires confirmation before deleting.
        """
        password_count = self.db.get_password_count()

        if password_count == 0:
            Graphics.read_border()
            print("\nNo passwords to delete.\n")
            Graphics.read_border()
            return

        print(f"\nTotal passwords in database: {password_count}\n")

        delete_choice: str = PasswordMode._get_user_input(
            "Delete by ID or delete all? (id/all) (q to quit): "
        ).lower()

        if delete_choice == "id":
            self._delete_by_id()
        elif delete_choice == "all":
            self._delete_all()
        else:
            print("\nInvalid choice. Please enter 'id' or 'all'.\n")

    def _delete_by_id(self) -> None:
        """Delete a specific password entry by ID with confirmation."""
        passwords = self.db.get_all_passwords()

        Graphics.read_border()
        print("\nAvailable passwords:\n")
        for password_entry in passwords:
            password_id, website, email, _, _ = password_entry
            print(f"  ID: {password_id} | Website: {website} | Email: {email}")
        Graphics.read_border()

        password_id_str: str = PasswordMode._get_user_input(
            "\nEnter the ID of the password to delete (q to quit): "
        )

        try:
            password_id = int(password_id_str)
        except ValueError:
            print("\nInvalid ID. Please enter a number.\n")
            return

        password = self.db.get_password_by_id(password_id)
        if not password:
            print(f"\n❌ Password with ID {password_id} not found.\n")
            return

        _, website, email, _, _ = password
        confirm: bool = PasswordMode._get_yes_no_input(
            f"\nAre you sure you want to delete ID {password_id} ({website})? (y/n): "
        )

        if confirm:
            if self.db.delete_password_by_id(password_id):
                print(f"\n✅ Password with ID {password_id} successfully deleted.\n")
            else:
                print(f"\n❌ Error deleting password with ID {password_id}.\n")
        else:
            print("\n⚠️  Deletion cancelled.\n")

    def _delete_all(self) -> None:
        """Delete all password entries with double confirmation."""
        confirm1: bool = PasswordMode._get_yes_no_input(
            "\n⚠️  Are you sure you want to delete ALL passwords? (y/n): "
        )

        if not confirm1:
            print("\n⚠️  Deletion cancelled.\n")
            return

        confirm2: bool = PasswordMode._get_yes_no_input(
            "This action CANNOT be undone. Are you absolutely sure? (y/n): "
        )

        if confirm2:
            if self.db.delete_all_passwords():
                print("\n✅ All passwords successfully deleted.\n")
            else:
                print("\n❌ Error deleting all passwords.\n")
        else:
            print("\n⚠️  Deletion cancelled.\n")

    def mode(self) -> None:
        """Route user choice to appropriate mode handler."""
        match self.choice.lower():
            case "view" | "v":
                self.view()
            case "add" | "a":
                self.add()
            case "delete" | "d":
                self.delete()
            case "quit" | "q":
                Graphics.closing()
                exit()
            case _:
                print(
                    "\nInvalid input. Please choose 'a' (add), 'v' (view), 'd' (delete), or 'q' (quit).\n"
                )

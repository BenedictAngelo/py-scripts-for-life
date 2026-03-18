import datetime
import random
import string

from cryptography.fernet import Fernet

from shared import closing, read_border, script_title

"""
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)"""
# write_key()


class Password_Generator:
    def __init__(
        self, max_character: int, numbers: bool = True, special_characters: bool = True
    ):
        self.max_character = max_character
        self.numbers = numbers
        self.special_characters = special_characters

    @staticmethod
    def encryptor():
        file = open("key.key", "rb")
        key = file.read()
        file.close()
        fer = Fernet(key)
        return fer

    def generator(self):
        fer = Password_Generator.encryptor()
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

        password = fer.encrypt(password.encode()).decode()

        return password


class Password_Manager(Password_Generator):
    def __init__(
        self,
        website: str,
        email: str,
        max_character: int,
        numbers: bool = True,
        special_characters: bool = True,
    ):
        super().__init__(max_character, numbers, special_characters)
        self.website = website
        self.email = email
        self.password = self.generator()
        self.time_now = datetime.datetime.now().strftime("%I:%M:%S %a %b-%d-%Y")

    def what_website(self) -> str:
        return self.website

    def what_email(self) -> str:
        return self.email

    def what_password(self) -> str:
        return self.password

    def what_time(self) -> str:
        return self.time_now


class Mode:
    def __init__(self, choice: str):
        self.choice = choice

    @staticmethod
    def view():
        fer = Password_Generator.encryptor()
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
                        print(f"Time created: {time_view}\n")
            read_border()
        except FileNotFoundError:
            read_border()
            print("\nNo 'passwords.txt' file was found.")
            print("Creating file...")
            with open("passwords.txt", "a") as f:
                f.write("")
                print("\nFile successfully created but empty for now\n")
        finally:
            pass

    @staticmethod
    def add():
        # Website input
        def website_input():
            while True:
                website = input("\nFor what website will you use it? (q to quit): ")
                if website.lower() == "q":
                    print("Exiting...")
                    closing()
                    exit()
                else:
                    break
            return website

        # Email input
        def email_input():
            while True:
                email = input("\nWhat email will you use it for? (q to quit): ")
                if email.lower() == "q":
                    closing()
                    print("Exiting...")
                    exit()
                else:
                    break
            return email

        # Max Character input
        def max_character_input():
            while True:
                max_character = input(
                    "\nHow many maximum characters in password do you want? (digits only or q to quit): "
                )
                if max_character.lower() == "q":
                    print("Exiting...")
                    closing()
                    exit()
                elif not max_character.isdigit():
                    print("\nInvalid input. Please enter digits only.")
                    continue
                else:
                    break
            return int(max_character)

        # If has number input
        def numbers_input():
            while True:
                numbers = input(
                    "\nDo you want digits in your password? (y/n) (q to quit): "
                ).lower()
                match numbers:
                    case "y":
                        numbers = True
                        break
                    case "n":
                        numbers = False
                        break
                    case "q":
                        print("Exiting...")
                        closing()
                        exit()
                    case _:
                        print("\nInvalid input. Please enter 'y', 'n', 'q' only.")
                        continue
            return numbers

        # if has special number input
        def special_characters_input():
            while True:
                special_characters = input(
                    "\nDo you want special characters in your password? (y/n) (q to quit): "
                ).lower()
                match special_characters:
                    case "y":
                        special_characters = True
                        break
                    case "n":
                        special_characters = False
                        break
                    case "q":
                        print("Exiting...")
                        closing()
                        exit()
                    case _:
                        print("\nInvalid input. Please enter 'y', 'n', 'q' only.")
                        continue
            return special_characters

        while True:
            website: str = website_input()
            email: str = email_input()
            max_character: int = max_character_input()
            numbers: bool = numbers_input()
            special_characters: bool = special_characters_input()

            # CALL THE WHOLE GENERATOR
            call_generator = Password_Manager(
                website, email, max_character, numbers, special_characters
            )
            write_website = call_generator.what_website()
            write_email = call_generator.what_email()
            write_password = call_generator.what_password()
            write_time = call_generator.what_time()

            with open("passwords.txt", "a") as f:
                f.write(
                    write_website
                    + "|"
                    + write_email
                    + "|"
                    + write_password
                    + "|"
                    + write_time
                    + "\n"
                )
                print("\nPassword successfully written!\n")
                break

    def mode(self):
        match self.choice.lower():
            case "view":
                Mode.view()
            case "add":
                Mode.add()
            case "q":
                print("Exiting...")
                closing()
                exit()
            case _:
                print("Invalid input.")
                pass


def app():
    title: str = "Password Manager"
    script_title(title)

    try:
        while True:
            choice = input(
                "Choose what mode do you want, 'add' or 'view'? (q to quit): "
            )
            Mode(choice).mode()
    except KeyboardInterrupt:
        print("\n\nProgram has been forcefully canceled.\n")
    finally:
        exit()


def main():
    app()


if __name__ == "__main__":
    main()

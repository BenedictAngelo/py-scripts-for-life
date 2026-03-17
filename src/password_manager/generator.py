import random
import string
from .crypto import fer
from .global_variables import exit_graphic
#input("How many characters do you want? (q to quit): ")
def password(max_char):
    while True:
        ascii = string.printable
        ascii_split = list(ascii[:-6])

        match max_char.lower():
            case "q":
                print("\nCancelling process...\n")
                print("Exiting....") 
                exit()
            case _:
                match max_char.isdigit():
                    case True:
                        generator = random.choices(ascii_split, k=int(max_char))
                        pwd = "".join(generator)
                        print(f"\nRandomized password generated: {pwd}\n")
                        pwd = fer.encrypt(pwd.encode()).decode()
                        print(f"Randomized password successfully encrypted:\n{pwd}")
                        print()
                        return pwd
                    case _:
                        print("\nInvalid Input, make sure to type digits or 'q' to quit\n")
                        pwd = ""
                        return pwd
    return pwd

def confirmation(max_char):
    while True:
        pwd = password(max_char)
        if pwd == "":
            max_char = input("Enter how many characters you want again in your password (q to quit): ")
            pwd = confirmation(max_char)
            return pwd

        confirm = input("Are you satisfied with the password generated?: (y/n) (q to quit): ").lower()

        if confirm == "q":
            print("\nCancelling process...\n")
            exit_graphic()
            exit()

        match confirm:
            case "y":
                break
            case "n":
                max_char = input("Enter how many characters you want again in your password (q to quit): ")
                pwd = confirmation(max_char)
                return pwd
            case _:
                print("\nInvalid Input, make sure to type 'y' or 'n' or 'q' to quit")
                continue
    return pwd




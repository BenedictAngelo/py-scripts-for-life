import datetime
from .generator import confirmation
from .crypto import fer
from .global_variables import exit_graphic



def view():
        try:
            with open("passwords.txt", "r") as f:
                border = "\n==========================================================================\n"
                read_border = "--------------------------------------------------------------------------"
                print(read_border)
                for line in f.readlines():
                    data = line.rstrip()
                    website_view, email_view, pwd_view, time_view = data.split("|")
                    print(
                        f"{border}Website: {website_view}\nEmail: {email_view}\nPassword: {fer.decrypt(pwd_view.encode()).decode()}\nTime created: {time_view}{border}"
                    )
                print(read_border)
        except FileNotFoundError:
            print("\nNo 'password.txt' file was found.")
            print("Creating file...")
            with open("passwords.txt", "a") as f:
                f.write("")
                print("\nFile successfully created but empty for now\n")
        finally:
            pass

    

def add():
    website = input("On what website will you use this? (q to quit): ")
    if website.lower() == "q":
        print("\nCancelling process...")
        exit_graphic()
        exit()

    email = input("What email will you use? (q to quit): ")
    if email.lower() == "q":
        print("\nCancelling process...\n")
        exit_graphic()
        exit()

    pwd = confirmation(input("How many characters do you want in your password? (q to quit): "))

    time_now = datetime.datetime.now().strftime("%I:%M:%S %a %b-%d-%Y")

    with open("passwords.txt", "a") as f:
        f.write(website + "|" + email + "|" + pwd + "|" + time_now + "\n")
        print("\nPassword successfully written!\n")

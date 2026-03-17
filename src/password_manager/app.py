from .options import view, add,exit_graphic
from .global_variables import entry_graphic
def app():
    try:
        entry_graphic()
        while True:
            mode = input(
                "\nWould you like to add or view a password? (view/add) (q to quit): "
            ).lower()

            match mode:
                case "q":
                    print("\nCanceling process...\n")
                    exit_graphic()
                    exit()
                case "view":
                    print("\nYou chose 'view':")
                    view()
                case "add":
                    print("\nYou chose 'add':\n")
                    add()
                case _:
                    print("\nInvalid input. Enter 'view' or 'add' or 'q' to quit.")
                    continue
    except KeyboardInterrupt:
        print("\n\nProgram has been forcefully canceled.\n")
        exit_graphic()
    finally:
        exit()

    return 0

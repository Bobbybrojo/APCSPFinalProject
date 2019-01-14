import sys
from Calc import calc


def main_menu():

    print("Welcome to the main menu!")

    gamemode = input("Choose your gamemode: ")

    if gamemode.lower() == "calc":
        calc()
    elif gamemode.lower() == "quit":
        sys.exit(0)
    else:
        main_menu()
    return 0


main_menu()




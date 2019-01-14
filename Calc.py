


def calc():
    # program start/introduction
    print(" #_______________________________________________# ")
    print(" |------You have accessed the calculator app-----| ")
    print(" |----------------Input 2 numbers----------------| ")
    print(" |--------------Choose an operator---------------| ")
    print(" #_______________________________________________# ")
    # instructions to user and user input stored in vars
    print("Type in the console to input your answers")
    num1 = input("Choose your first number:  ")
    operator = input("Choose your operator (*, /, +, -):  ")
    num2 = input("Choose your second number:  ")
    # program runs appropriate calculations
    if operator == "*":
        answer = (int(num1) * int(num2))
        print(num1 + " + " + num2 + " = " + str(answer))

    elif operator == "/":
        answer = (int(num1) / int(num2))
        print(num1 + " / " + num2 + " = " + str(answer))

    elif operator == "+":
        answer = (int(num1) + int(num2))
        print(num1 + " + " + num2 + " = " + str(answer))

    elif operator == "-":
        answer = (int(num1) - int(num2))
        print(num1 + " - " + num2 + " = " + str(answer))
    else:
        print("Sorry you entered something wrong :( try entering the symbols for multiplication")
    return_to_main_menu = input("Would you like to return to the main menu? Y/N: ")
    if return_to_main_menu.lower() == "y" or return_to_main_menu == "yes":
        main_menu()
    else:
        print(" ")
        calc()
    return 0;
















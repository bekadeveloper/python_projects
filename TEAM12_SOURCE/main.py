# Team 12 Project
# Implementing LMS Operations

import data
import functions as func
from termcolor import colored

accountNotCreated = True

print('\t' * 10, colored("Welcome to the i-Class log-in page!", 'blue'))
waiting = input("Press enter to continue...")

if not waiting:
    typeofAccount = input(f'''Do you want to create an account or you already have it? 
If you already have an account please type {colored('"OLD"', 'green')}, otherwise {colored('"NEW"', 'green')}\n''')

while accountNotCreated:

    if typeofAccount == "NEW":
        print("Please, fill out all this data to create a new account...\n")
        name = input("\t\tYour full name: ")
        email = input("\t\tE-mail address: ")
        login = input("\t\tChoose a login: ")
        password = input("\t\tChoose a min. 6-digit password: ")
        verifyPassword = input("\t\tVerify your password: ")
        waiting = input("\nPress enter to submit...")

        if not waiting:
            if len(password) >= 6 and verifyPassword == password:
                accountNotCreated = False
                print(colored("You've successfully created an account", 'blue'))
                waiting = input("Press enter to log-in into the system...\n")
                if not waiting:
                    loginConfirm = input("\t\tEnter your login: ")
                    passwordConfirm = input("\t\tEnter your password: ")
                    waiting = input("\nPress enter to continue...")
                    if not waiting:
                        notLoggedYet = True
                        while notLoggedYet:
                            if loginConfirm == login and passwordConfirm == password:
                                notLoggedYet = False
                                print(colored(f"Welcome to the i-Class system {name}!", 'blue'))
                                waiting = input("Press enter to see the list of your classes...")
                                if not waiting:
                                    n = 1
                                    for i in data.courses:
                                        print("\t\t", n, "-", colored(i, 'yellow'))
                                        n += 1
                                    courseChoice = input("Enter the number or name of class to see operations...\n")

                                    if courseChoice:
                                        n = 1
                                        for i in data.operations:
                                            print("\t\t", n, "-", colored(i, 'yellow'))
                                            n += 1
                                        operationChoice = input("Enter the number or name of operation to continue...\n")

                                        if operationChoice:
                                            print(func.doOperation(courseChoice, operationChoice))

                            else:
                                print(colored("Login or password isn't correct!", 'red'))
                                waiting = input("Press enter to try again...")
                                if not waiting:
                                    pass
            else:
                print(colored("The registration process was completed unsuccessfully!", 'red'))
                waiting = input("Press enter to try again...")
                if not waiting:
                    pass

    elif typeofAccount == "OLD":
        accountNotCreated = False
        notLoggedYet = True

        while notLoggedYet:
            login = input("\t\tEnter your login: ")
            password = input("\t\tEnter your password: ")
            waiting = input("\nPress enter to submit...")

            if not waiting:
                if login in data.logins and password in data.passwords:

                    correctLoginAndPass = False

                    if login == data.logins[0] and password == data.passwords[0]:
                        print(colored(f"Welcome to the i-Class system {data.names[0]}!", 'blue'))
                        correctLoginAndPass = True

                    elif login == data.logins[1] and password == data.passwords[1]:
                        print(colored(f"Welcome to the i-Class system {data.names[1]}!", 'blue'))
                        correctLoginAndPass = True

                    elif login == data.logins[2] and password == data.passwords[2]:
                        print(colored(f"Welcome to the i-Class system {data.names[2]}!", 'blue'))
                        correctLoginAndPass = True

                    elif login == data.logins[3] and password == data.passwords[3]:
                        print(colored(f"Welcome to the i-Class system {data.names[3]}!", 'blue'))
                        correctLoginAndPass = True

                    if correctLoginAndPass:
                        notLoggedYet = False
                        waiting = input("Press enter to see the list of your classes...")

                        if not waiting:
                            n = 1
                            print()
                            for i in data.courses:
                                print("\t\t", n, "-", colored(i, 'yellow'))
                                n += 1
                            print()
                            courseChoice = input("Enter the number or name of class to see operations...\n")

                            if courseChoice:
                                n = 1
                                for i in data.operations:
                                    print("\t\t", n, "-", colored(i, 'yellow'))
                                    n += 1
                                print()
                                operationChoice = input("Enter the number or name of operation to continue...\n")

                                if operationChoice:
                                    print(func.doOperation(courseChoice, operationChoice))
                    else:
                        waiting = input(colored("Login and password doesn't match!\nPress enter to try again...", 'red'))
                else:
                    waiting = input(colored("Login and password are not correct!\nPress enter to try again...", 'red'))
    else:
        break
import data
from termcolor import colored

def doOperation(course, operation):

    if course in data.courses[0] or course == "1":
        print(f'''\t\tClass name: {colored("English Communication: Advanced", 'yellow')}\t\t\t\tClass number: {colored("GEB1109", 'yellow')}\n\t\tCredits: {colored("3.0", 'yellow')}''')
        if operation in data.operations[0] or operation == "1":
            print(data.english[0])
        elif operation in data.operations[1] or operation == "2":
            print(data.english[1])
        elif operation in data.operations[2] or operation == "3":
            print(data.english[2])
        elif operation in data.operations[3] or operation == "4":
            toWhom = input("To whom you want to give a question: ")
            message = input("Type your question here:\n")
            send = input("Press enter to send it...")
            print(f"\n\t\tSent to: {colored(toWhom, 'yellow')}\n\t\tMessage: {colored(message, 'yellow')}\n")
        elif operation in data.operations[4] or operation == "5":
            print(data.english[3])
        else:
            print(colored("Operation not found!", 'red'))

    elif course in data.courses[1] or course == "2":
        print(f'''\t\tClass name: {colored("Basic Korean", 'yellow')}\t\t\t\tClass number: {colored("GEG2008", 'yellow')}\n\t\tCredits: {colored("3.0", 'yellow')}''')
        if operation in data.operations[0] or operation == "1":
            print(data.korean[0])
        elif operation in data.operations[1] or operation == "2":
            print(data.korean[1])
        elif operation in data.operations[2] or operation == "3":
            print(data.korean[2])
        elif operation in data.operations[3] or operation == "4":
            toWhom = input("To whom you want to give a question: ")
            message = input("Type your question here:\n")
            send = input("Press enter to send it...")
            print(f"\n\t\tSent to: {colored(toWhom, 'yellow')}\n\t\tMessage: {colored(message, 'yellow')}\n")
        elif operation in data.operations[4] or operation == "5":
            print(data.korean[3])
        else:
            print(colored("Operation not found!", 'red'))

    elif course in data.courses[2] or course == "3":
        print(f'''\t\tClass name: {colored("Phronesis Seminar 1: Value Formation & Career Exploration", 'yellow')}\t\tClass number: {colored("GEB1115", 'yellow')}\n\t\tCredits: {colored("1.0", 'yellow')}''')
        if operation in data.operations[0] or operation == "1":
            print(data.phronesis[0])
        elif operation in data.operations[1] or operation == "2":
            print(data.phronesis[1])
        elif operation in data.operations[2] or operation == "3":
            print(data.phronesis[2])
        elif operation in data.operations[3] or operation == "4":
            toWhom = input("To whom you want to give a question: ")
            message = input("Type your question here:\n")
            send = input("Press enter to send it...")
            print(f"\n\t\tSent to: {colored(toWhom, 'yellow')}\n\t\tMessage: {colored(message, 'yellow')}\n")
        # elif operation in data.operations[4] or operation == "5":
        #     print(data.phronesis[3])
        else:
            print(colored("Operation not found!", 'red'))

    elif course in data.courses[3] or course == "4":
        print(f'''\t\tClass name: {colored("Reading Seminar: Humanities & Culture", 'yellow')}\t\tClass number: {colored("GEC1018", 'yellow')}\n\t\tCredits: {colored("3.0", 'yellow')}''')
        if operation in data.operations[0] or operation == "1":
            print(data.reading[0])
        elif operation in data.operations[1] or operation == "2":
            print(data.reading[1])
        elif operation in data.operations[2] or operation == "3":
            print(data.reading[2])
        elif operation in data.operations[3] or operation == "4":
            toWhom = input("To whom you want to give a question: ")
            message = input("Type your question here:\n")
            send = input("Press enter to send it...")
            print(f"\n\t\tSent to: {colored(toWhom, 'yellow')}\n\t\tMessage: {colored(message, 'yellow')}\n")
        elif operation in data.operations[4] or operation == "5":
            print(data.reading[3])
        else:
            print(colored("Operation not found!", 'red'))

    elif course in data.courses[4] or course == "5":
        print(f'''\t\tClass name: {colored("Understandings of Economics", 'yellow')}\t\t\t\tClass number: {colored("GEG1030", 'yellow')}\n\t\tCredits: {colored("3.0", 'yellow')}''')
        if operation in data.operations[0] or operation == "1":
            print(data.economics[0])
        elif operation in data.operations[1] or operation == "2":
            print(data.economics[1])
        elif operation in data.operations[2] or operation == "3":
            print(data.economics[2])
        elif operation in data.operations[3] or operation == "4":
            toWhom = input("To whom you want to give a question: ")
            message = input("Type your question here:\n")
            send = input("Press enter to send it...")
            print(f"\n\t\tSent to: {colored(toWhom, 'yellow')}\n\t\tMessage: {colored(message, 'yellow')}\n")
        elif operation in data.operations[4] or operation == "5":
            print(data.economics[3])
        else:
            print(colored("Operation not found!", 'red'))

    elif course in data.courses[5] or course == "6":
        print(f'''\t\tClass name: {colored("Introductory Engineering Mathematics", 'yellow')}\t\t\t\tClass number: {colored("IGS1130", 'yellow')}\n\t\tCredits: {colored("3.0", 'yellow')}''')
        if operation in data.operations[0] or operation == "1":
            print(data.math[0])
        elif operation in data.operations[1] or operation == "2":
            print(data.math[1])
        elif operation in data.operations[2] or operation == "3":
            print(data.math[2])
        elif operation in data.operations[3] or operation == "4":
            toWhom = input("To whom you want to give a question: ")
            message = input("Type your question here:\n")
            send = input("Press enter to send it...")
            print(f"\n\t\tSent to: {colored(toWhom, 'yellow')}\n\t\tMessage: {colored(message, 'yellow')}\n")
        elif operation in data.operations[4] or operation == "5":
            print(data.math[3])
        else:
            print(colored("Operation not found!", 'red'))

    elif course in data.courses[6] or course == "7":
        print(f'''\t\tClass name: {colored("Software Programming", 'yellow')}\t\t\t\tClass number: {colored("IGS1131", 'yellow')}\n\t\tCredits: {colored("3.0", 'yellow')}''')
        if operation in data.operations[0] or operation == "1":
            print(data.programming[0])
        elif operation in data.operations[1] or operation == "2":
            print(data.programming[1])
        elif operation in data.operations[2] or operation == "3":
            print(data.programming[2])
        elif operation in data.operations[3] or operation == "4":
            toWhom = input("To whom you want to give a question: ")
            message = input("Type your question here:\n")
            send = input("Press enter to send it...")
            print(f"\n\t\tSent to: {colored(toWhom, 'yellow')}\n\t\tMessage: {colored(message, 'yellow')}\n")
        elif operation in data.operations[4] or operation == "5":
            print(data.programming[3])
        else:
            print(colored("Operation not found!", 'red'))
    else:
        print(colored("Class not found"))
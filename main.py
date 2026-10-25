def showOptions():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
    return None

def askChoice():
    Choice = input("Your choice: ")
    if Choice.isnumeric():
        Choice = int(Choice)
    else:
        Choice = -1
    return Choice

def main():
    print("Program starting.")
    Count = 0
    while True:
        showOptions()
        Choice = askChoice()
        if Choice == 0:
            print("Exiting program.")
            break
        elif Choice == 1:
            print("Current count - {}".format(Count))
        elif Choice == 2:
            Count += 1
            print("Count increased!")
        elif Choice == 3:
            Count = 0
            print("Cleared count!")
        else:
            print("Unknown option!")
        print("")
    print("")
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()

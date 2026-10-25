def showOptions():
    print("options:")
    print("1 - show-count")
    print("2 - increase-count")
    print("3 - reset-count")
    print("0 - exit")

def askChoice():
    choice = input("your choice: ")
    if choice.isnumeric():
        return int(choice)
    else:
        print("Unknown option!")
        return -1

def main():
    print("program starting.")
    count = 0
    while True:
        showOptions()
        choice = askChoice()
        if choice == 1:
            print(f"current-count: {count}")
        elif choice == 2:
            count += 1
        elif choice == 3:
            count = 0
        elif choice == 0:
            print("exiting program.")
            break
    print("program ending.")

if __name__ == "__main__":
    main()
 

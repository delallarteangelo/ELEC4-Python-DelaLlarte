# Name: Angelo V. Dela Llarte
# Section: IV-BSIT A
# Activity: P4: Safe Menu Program
# Date: November 17, 2026
    


def divide_numbers(): # divide two numbers with exception handling for invalid input and division by zero
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = a / b
    except ValueError:
        print("Error: please enter numbers only.")
    except ZeroDivisionError:
        print("Error: you cannot divide by zero.")
    else:
        print(f"Result: {a} / {b} = {result}")
    finally:
        print("[Division attempt finished]")


def open_file(): # open a file with exception handling for file not found, permission error, and is a directory error
    filename = input("Enter file name: ").strip()
    try:
        with open(filename, "r") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: the file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: no permission to open '{filename}'.")
    except IsADirectoryError:
        print(f"Error: '{filename}' is a folder, not a file.")
    else:
        print("\n--- File contents ---")
        print(content)
    finally:
        print("[File operation finished]")

 
def main(): #main function to display the menu and call the appropriate functions based on user choice
    while True:
        print("\n=== Safe Menu Program ===")
        print("1. Divide two numbers")
        print("2. Open a file")
        print("3. Exit")
        choice = input("Choose (1-3): ").strip()
        if choice == "1":
            divide_numbers()
        elif choice == "2":
            open_file()
        elif choice == "3":
            print("Program Terminated.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


main()
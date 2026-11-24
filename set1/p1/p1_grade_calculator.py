# Name: Angelo V. Dela Llarte
# Section: IV-BSIT A
# Activity: P1 - Student Grade Calculator
# Date: November 16, 2026
    



PASSING_AVERAGE = 75  # the minimum average grade needed to pass


def get_valid_grade(prompt):
    # it asks for ONE grade and will keep on asking until it is a number from 0 to 100.
    while True:
        try:
            grade = float(input(prompt))
        except ValueError:  # validation for the user if they typed letters or symbols
            print("Invalid input. Please enter a number.")
            continue
        # validation for the user if they typed a number outside of the range 0-100
        if 0 <= grade <= 100:
            return grade
        print("Invalid grade. It must be from 0 to 100.")


def enter_grades():
    # will ask the user how many grades they want to enter and will keep on asking until they enter a number greater than 0.
    while True:
        try:
            count = int(input("How many grades will you enter? "))
              # validation for the user if they typed a character or a number less than 1
            if count > 0:
                break
            print("Enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")
    return [get_valid_grade(f"  Grade {i}: ") for i in range(1, count + 1)]


def compute_average(grades):
   # formula to Compute the average of the grades.

    total = sum(grades) 
    return total / len(grades)


def get_highest(grades):
    #function to find the highest grade in the list of grades.

    return max(grades)


def get_lowest(grades):
    #function to find the lowest grade in the list of grades.


    return min(grades)


def get_status(grades, passing=PASSING_AVERAGE):
   #will determine if the student has passed or failed based on the 
   # average of their grades and the passing average defined at the top of the file.

    return "PASSED" if compute_average(grades) >= passing else "FAILED"


def view_results(grades):
# will display the grades, average, highest, lowest, and status of the student.
    if not grades:
        print("No grades yet. Choose option 1 first.")
        return
    print("\n--- Results ---")
    print("Grades  :", grades)
    print(f"Average : {compute_average(grades):.2f}")
    print(f"Highest : {get_highest(grades):.2f}")
    print(f"Lowest  : {get_lowest(grades):.2f}")
    print("Status  :", get_status(grades))


def main():
# the main function that will run the program and display the menu to the user.

    grades = []
    while True:
        print("\n=== Student Grade Calculator ===")
        print("1. Enter grades")
        print("2. View results")
        print("3. Exit")
        choice = input("Choose (1-3): ").strip()
        if choice == "1":
            grades = enter_grades()
        elif choice == "2":
            view_results(grades)
        elif choice == "3":
            print("Program terminated.")
            break
        else:
            print("Invalid choice. Try again.")


main()



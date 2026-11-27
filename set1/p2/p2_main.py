# Name: Angelo V. Dela Llarte
# Section: IV-BSIT A
# Activity: P2: Custom Module: student_utils
# Date: November 1, 2026
    


import student_utils  # need to import student_utils para magamit yung mga functions na nasa student_utils.py
from student_utils import get_highest, get_lowest  # iimport din yung mga functions na get_highest at 
                                                    #get_lowest para magamit sa p2_main.py
from datetime import datetime  # built-in module


#input validation ng grade na ipapasok ng user. Kung hindi valid, magpprint ng error message at hihingi ulit ng input.
def get_valid_grade(prompt):
    while True:
        try:
            grade = float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if 0 <= grade <= 100:
            return grade
        print("A grade must be from 0 to 100.")

#unang makikita ng user ay ang main function na magpprint ng student name, number of grades, at mga grades na ipapasok ng user.
def main():
    name = input("Student name: ").strip()
    while True:
        try:
            numberofGrades = int(input("How many grades? "))
            if numberofGrades > 0:
                break
            print("Enter a number greater than 0.")
        except ValueError:
            print("Please enter a whole number.")

    grades = [get_valid_grade(f"  Grade {i}: ") for i in range(1, numberofGrades + 1)]

    print("\n===== Grade Report =====")
    print("Student   :", name)
    print(f"Generated : {datetime.now().strftime('%B %d, %Y %I:%M %p')}")
    print(f"Average   : {student_utils.calculate_average(grades):.2f}")
    print(f"Highest   : {get_highest(grades):.2f}")
    print(f"Lowest    : {get_lowest(grades):.2f}")
    print("Status    :", student_utils.determine_status(grades))

# This ensures that the main function runs only when this file is executed directly, not when imported as a module.
if __name__ == "__main__":
    main()

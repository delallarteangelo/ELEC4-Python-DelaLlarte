# Name: Angelo V. Dela Llarte
# Section: IV-BSIT A
# Activity: P2: Custom Module: student_utils
# Date: November 16, 2026

PASSING_AVERAGE = 75


def calculate_average(grades):
    return sum(grades) / len(grades)


def determine_status(grades, passing=PASSING_AVERAGE):
    return "PASSED" if calculate_average(grades) >= passing else "FAILED"


def get_highest(grades):
    return max(grades)


def get_lowest(grades):
    return min(grades)




# Name: Angelo V. Dela Llarte
# Section: IV-BSIT A
# Activity: P3: Student Record Manager 
# Date: November 17, 2026
    


# normalize function to convert the name to lowercase and remove extra spaces na gagamitin for duplication checking
def normalize(name):
    return " ".join(name.lower().split())


def add_student(students, keys, name):  #add a name to the  list and the set, unless it already exists 
 
    name = " ".join(name.split())
    if not name:
        print("Name cannot be empty.")
        return
    #it will use the normalize function to convert the name to lowercase and remove extra spaces for duplication checking
    key = normalize(name)
    if key in keys:
        print(f"'{name}' already exists. Not added.")
        return
    
    students.append([name.title(), key])
    keys.add(key)
    print(f"'{name.title()}' added.")


def remove_student(students, keys, name): # remove a name from the list and the set, if it exists
  
    key = normalize(name)
    if key not in keys: # if the name does not exist in the set, it will print "Student not found."
        print("Student not found.")
        return
    #for row in students, if the lowercase key matches the name to be removed, 
    #it will remove that row from the list and break the loop from entering another input
    for row in students:
        if row[1] == key:
            students.remove(row)
            break
    keys.remove(key)
    print(f"'{name.title()}' removed.")


def search_student(students, term):
  #search for a name in the list, ignoring case and extra spaces using 
  # the normalize function, and print the number of matches found 
    term = normalize(term)
    if not term:
        print("Enter something to search.")
        return
    matches = []
    for row in students:
        if term in row[1]:
            matches.append(row[0])
    matches.sort(key=str.lower)

    if matches:
        print(f"Found {len(matches)} match(es):")
        for s in matches:
            print(" -", s)
    else:
        print("No matches found.")


def display_students(students):  # will display all the students in the list, sorted
                                 # alphabetically, and show the total number of students.
    if not students:
        print("No students yet.")
        return
    print("\n--- Students (A-Z) ---")
    #will print the students in the list, sorted alphabetically by their lowercase key, and numbered starting from 1
    for i, row in enumerate(sorted(students, key=lambda r: r[1]), start=1):
        print(f"{i}. {row[0]}")
    print(f"Total: {len(students)}")


#main menu function that will run the program and display the menu to the user, 
# allowing them to add, remove, search, or display students, or exit the program.
def main():
    students = []  # list or array each row is [display name, lowercase key]
    keys = set()   # set: lowercase copy of each name, for duplicate checking
    while True:
        print("\n=== Student Record Manager ===")
        print("1. Add student")
        print("2. Remove student")
        print("3. Search student")
        print("4. Display all students")
        print("5. Exit")
        choice = input("Choose (1-5): ").strip()

        if choice == "1":
            add_student(students, keys, input("Name to add: "))

        elif choice == "2":
            remove_student(students, keys, input("Name to remove: "))

        elif choice == "3":
            search_student(students, input("Search: "))

        elif choice == "4":
            display_students(students)

        elif choice == "5":
            print("Program Terminated.")
            break
        else:
            print("Invalid choice. Try again.")


main()

# A list is an ordered collection that allows duplicates and can be sorted or indexed, while a
# set is unordered and automatically ignores duplicate values. In my program, "students" is a
# 2D list where each row is [name, lowercase key], and I add rows to it using
# append() so I can display them sorted and numbered. The set "keys" stores the lowercase
# version of each name, so checking if a name like "juan cruz" already exists is fast and
# not case-sensitive.

#import modules
from data import load_students
from menu import display_menu
from crud import (
    add_student,
    list_students,
    find_student,
    update_student,
    delete_student
)

def main():
    """
    Main function that controls the system.
    """
    #Load data from file
    students = load_students()
    option = ""

    #main loop
    while option != "6":
        display_menu()
        option = input("Choose an option: ")

        if option == "1":
            add_student(students)
        elif option == "2":
            list_students(students)
        elif option == "3":
            find_student(students)
        elif option == "4":
            update_student(students)
        elif option == "5":
            delete_student(students)
        elif option == "6":
            print("Goodbye!")
        else:
            print("Invalid option.\n")

#program entry point:
if __name__ == "__main__":
    main()
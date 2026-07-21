from src.models.student import Student
from src.utils.calculations.average import average
from src.utils.calculations.total import total
from src.controllers.add_student import add_student
from src.controllers.disp_many import display_students
from src.exception.exception import MissingNameError
from src.config.logger import logging


logger = logging.getLogger("main")
def main():
    students: list[Student] = []
    while True:
        print("Student Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Calculate Average Marks")
        print("4. Calculate Total Marks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            marks = float(input("Enter student marks: "))
            school = input("Enter student school: ")
            try:
                students = add_student(students, name, age, marks, school)
            except MissingNameError as e:
                print(e)
                logger.error("Student is missing")
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            print(f"Average Marks: {average(students)}")
        elif choice == "4":
            print(f"Total Marks: {total(students)}")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.\n")

if(__name__ == "__main__"):
    main()
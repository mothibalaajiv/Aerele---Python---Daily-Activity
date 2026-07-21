import json
import os

DATA_FILE = "students.json"


def load_students():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_students(students):
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)


def add_student():
    students = load_students()

    name = input("Enter student name: ").strip()

    age = int(input("Enter age: "))

    marks = float(input("Enter marks: "))

    student = {
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)

    save_students(students)

    print("Student added successfully.\n")


def list_students():
    students = load_students()

    if not students:
        print("No students found.\n")
        return

    print("\nStudent List")
    print("-" * 40)

    for student in students:
        print(
            f"Name: {student['name']}, "
            f"Age: {student['age']}, "
            f"Marks: {student['marks']}"
        )

    print()


def calculate_average():
    students = load_students()

    if not students:
        print("No students available.\n")
        return

    total = sum(student["marks"] for student in students)

    average = total / len(students)

    print(f"Average Marks: {average:.2f}\n")


def find_topper():
    students = load_students()

    if not students:
        print("No students available.\n")
        return

    topper = max(students, key=lambda student: student["marks"])

    print("\nTopper")
    print("-" * 20)
    print(f"Name : {topper['name']}")
    print(f"Marks: {topper['marks']}\n")


def delete_student():
    students = load_students()

    name = input("Enter student name to delete: ").strip()

    updated_students = [
        student for student in students
        if student["name"].lower() != name.lower()
    ]

    if len(updated_students) == len(students):
        print("Student not found.\n")
        return

    save_students(updated_students)

    print("Student deleted successfully.\n")


def menu():
    while True:

        print("===== Student Management =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Average Marks")
        print("4. Find Topper")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            list_students()

        elif choice == "3":
            calculate_average()

        elif choice == "4":
            find_topper()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    menu()
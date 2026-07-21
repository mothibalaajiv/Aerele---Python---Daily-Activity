from src.models.student import Student

def display_students(students: list[Student]) -> None:
    if not students:
        print("No students to display.")
        return

    for student in students:
        print(f"Name: {student.name}, Age: {student.age}, Marks: {student.marks}, School: {student.school}")


from src.models.student import Student
def decorator(func):
    def wrp(*args,**kwargs):
        students = args
        if not students:
            raise ValueError("Student list is empty")
        return func(*args,**kwargs)
    return wrp

@decorator
def average(students: list[Student]) -> float:
    total_marks = sum(student.marks for student in students)
    print(total_marks)
    return total_marks / len(students)


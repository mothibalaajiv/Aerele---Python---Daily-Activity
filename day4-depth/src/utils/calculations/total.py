from src.models.student import Student

def decorator(func):
    def wrp(*args,**kwargs):
        def inner(students: list[Student]) -> float:
            if not students:
                raise ValueError("Student list is empty")
            return func(students)
        return inner
    return wrp

@decorator
def total(students: list[Student]) -> float:

    return sum(student.marks for student in students)
from src.models.student import Student
from src.exception.exception import MissingNameError
def decorator(func):
    def wrp(*args, **kwargs):
        x,name,age,marks,school=args
        if(name=="" or age<=0 or marks<0 or school==""):
            raise MissingNameError("Student name is missing")
        
        return func(*args, **kwargs)
    return wrp

@decorator
def add_student(students: list[Student], name: str, age: int, marks: float, school: str) -> list[Student]:
    new_student = Student(name=name, age=age, marks=marks, school=school)
    students.append(new_student)
    print(students)
    return students
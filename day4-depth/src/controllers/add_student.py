from src.models.student import Student

def decorator(func):
    def wrp(*args, **kwargs):
        x,name,age,marks,school=args
        if(name=="" or age<=0 or marks<0 or school==""):
            raise ValueError("Invalid student data")
        return func(*args, **kwargs)
    return wrp

@decorator
def add_student(students: list[Student], name: str, age: int, marks: float, school: str) -> None:
    new_student = Student(name=name, age=age, marks=marks, school=school)
    students.append(new_student)
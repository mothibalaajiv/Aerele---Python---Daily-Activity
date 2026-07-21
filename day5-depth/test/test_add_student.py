from src.models.student import Student
from src.controllers.add_student import add_student
def test_add_student():
    students=[]
    assert add_student(students,"Mothi",22,22,"BVB") == [Student(name="Mothi", age=22, marks=22.0, school="BVB")]
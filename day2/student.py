def calculate_student_result(name, marks):
    total = 0

    for mark in marks:
        total += mark

    average = total / len(marks)

    if average >= 90:
        grade = "A"

    elif average >= 75:
        grade = "B"

    elif average >= 50:
        grade = "C"

    else:
        grade = "F"

    print("----------------------")
    print("Student:", name)
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", average)
    print("Grade:", grade)
    print("----------------------")

    return {
        "name": name,
        "total": total,
        "average": average,
        "grade": grade
    }
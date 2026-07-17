from typing import List


def calculate_total(marks: List[int]) -> int:
    
    return sum(marks)


def calculate_average(total: int, subjects: int) -> float:
    
    return total / subjects


def calculate_grade(average: float) -> str:

    if average >= 90:
        return "A"

    if average >= 75:
        return "B"

    if average >= 50:
        return "C"

    return "F"


def display_result(result: dict) -> None:

    print("\n----- RESULT -----")
    print("Student :", result["name"])
    print("Total   :", result["total"])
    print("Average :", result["average"])
    print("Grade   :", result["grade"])
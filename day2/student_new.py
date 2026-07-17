from typing import List, Dict

from decorators import log_function
from helpers import (
    calculate_total,
    calculate_average,
    calculate_grade,
    display_result,
)


@log_function
def build_result(name: str, marks: List[int]) -> Dict:

    total = calculate_total(marks)

    average = calculate_average(total, len(marks))

    grade = calculate_grade(average)

    result = {
        "name": name,
        "total": total,
        "average": average,
        "grade": grade,
    }

    return result


@log_function
def process_student(name: str, marks: List[int]) -> Dict:

    result = build_result(name, marks)

    display_result(result)

    return result
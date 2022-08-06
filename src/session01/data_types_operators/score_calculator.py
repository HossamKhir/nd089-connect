#! /usr/bin/env python3
"""a script to calculate scores of students

https://collegeshortcuts.com/blog/gpa-converter
"""

import json
import random
import sys
from typing import Tuple, Union

random.seed(42)


def get_subject_grade(mark: int, score: int) -> Tuple[float, str, float]:
    """given a `mark` and a `score`, calculate percentile, letter grade,
    unweighted GPA

    Parameters
    ----------

    Returns
    -------
    out: tuple(float, str, float)
    """
    # TODO implement the functionality
    return 0.0, "TODO", 0.0


def get_student_grade(grades: Union[list, tuple]) -> Tuple[float, str, float]:
    """Given a student's `grades`, calculate the overall percentile, letter
    grade, unweighted GPA

    Parameters
    ----------

    Returns
    -------
    out: tuple(float, str, float)
    """
    # TODO implement the functionality
    return 0.0, "TODO", 0.0


def get_overall_grade(grades: dict) -> Tuple[float, str, float]:
    """calculates the overall grade of student

    Parameters
    ----------
    path: str

    Returns
    -------
    out: tuple(float, str, float)
    """
    gpa = []
    for subject in grades:
        grade = get_subject_grade(**grades[subject])
        grades[subject]["grade"] = grade
        gpa.append(grade[2])
    return get_student_grade(gpa)


if __name__ == "__main__":
    path = sys.argv[1]
    with open(path) as file:
        grades = json.loads(file.read())
    key, value = random.choice(list(grades.items()))
    overall_grade = get_overall_grade(value)
    print(key, "\b's overall grade: ", overall_grade)

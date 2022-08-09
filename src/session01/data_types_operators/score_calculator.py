#! /usr/bin/env python3
"""a script to calculate scores of students

https://collegeshortcuts.com/blog/gpa-converter
"""

import json
import random
import sys
from typing import Tuple, Union

random.seed(42)


def get_subject_grade(full_mark: int, mark: int) -> Tuple[float, str, float]:
    """given a `mark` and a `score`, calculate percentile, letter grade,
    unweighted GPA

    Parameters
    ----------

    Returns
    -------
    out: tuple(float, str, float)
    """
    # TODO implement the functionality
    # TODO calculate percentile
    perc = (mark / full_mark) * 100
    # TODO calculate unweighted GPA
    # HINT: 0 -> 0 fullmark -> 100%
    # HINT: 0 -> 0 fullmark -> 4.0
    gpa = 4 * perc / 100
    # NOTE: my own way of achieving just that
    # grade = mark / full_mark
    # perc = 100 * grade
    # gpa = 4 * grade
    return perc, "TODO", gpa


def get_student_grade(grades: Union[list, tuple]) -> Tuple[float, str, float]:
    """Given a student's `grades`, calculate the overall percentile, letter
    grade, unweighted GPA

    Parameters
    ----------
    grades: list | tuple
        a collection of GPAs for a single student

    Returns
    -------
    out: tuple(float, str, float)
    """
    # TODO implement the functionality
    # TODO AVG of GPA

    # NOTE this is old school average calculation, but kept for the sake of
    # short assignment demonstration
    avg_gpa = 0
    for grade in grades:
        avg_gpa += grade  # short assignment avg = avg+grade
        # *= -= /= //= %= <<= &=
    avg_gpa /= len(grades)
    # avg = sum(grades)/len(grades) # NOTE: this is more like python
    # TODO AVG of percentiles
    # NOTE: the next line is kept to demonstrate list comprehension
    perc = [i * 25 for i in grades]
    avg_perc = sum(perc) / len(perc)  # equivalently, 25 * avg_gpa
    # List comprehension
    # [expression (iter_var) for iter_var in collection]
    # Dict comprehension
    # {key:value for key, value in zip()/enumerate()}

    return avg_perc, "TODO", avg_gpa  # <- tuple


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
    # NOTE: classic way of using print
    # print(key, "\b's overall grade: ", overall_grade)
    # NOTE: collection expansion
    perc, letter, gpa = overall_grade
    # NOTE: str.format usages
    print("{}'s grades are {:.2f}, {}, {:.2f}".format(key, perc, letter, gpa))
    print(
        "{name}'s grades are {perc:.2f}, {letter}, {gpa:.2f}".format(
            name=key, perc=perc, letter=letter, gpa=gpa
        )
    )
    # NOTE: introducing f-strings (valid in python 3.6+)
    print(f"{key}'s grades are {perc:.3f}, {letter}, {gpa:.2f}")

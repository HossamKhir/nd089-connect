#! /usr/bin/env python3
"""making a collection of admitted candidates and their scores"""

import json
import sys

from session01.data_types_operators import get_overall_grade, admit_chance

if __name__ == "__main__":
    path = sys.argv[1]
    with open(path) as file:
        grades = json.loads(file.read())
    for candidate, scores in grades.items():
        grade = get_overall_grade(scores)
        chance = admit_chance(grade)
        # TODO unless chance is "low", the candidate should be admitted
        # TODO candidates should be stored alongside their grades
        pass

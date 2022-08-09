#! /usr/bin/env python3
"""get a collection of admitted candidates"""

import json
import sys

from session01.data_types_operators import admit_chance, get_overall_grade

if __name__ == "__main__":
    path = sys.argv[1]
    with open(path) as file:
        grades = json.loads(file.read())
    for candidate, scores in grades.items():
        grade = get_overall_grade(scores)
        chance = admit_chance(grade)
        # TODO unless chance is "low", the candidate should be admitted
        pass

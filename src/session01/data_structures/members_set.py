#! /usr/bin/env python3
"""get a unique unordered collection of admitted candidates"""
import json
import sys

from session01.data_types_operators import admit_chance, get_overall_grade

if __name__ == "__main__":
    path = sys.argv[1]
    with open(path) as file:
        grades = json.loads(file.read())
    grades = list(grades.items())
    grades.extend(grades[-2:])
    for candidate, scores in grades:
        grade = get_overall_grade(scores)
        chance = admit_chance(grade)
        # TODO unless chance is "low", the candidate should be admitted
        # TODO make sure there are no duplication in our collection
        pass

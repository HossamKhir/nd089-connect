#! /usr/bin/env python3
"""get a collection of admitted candidates"""

import json
import sys

from session01 import admit_chance, get_overall_grade

if __name__ == "__main__":
    path = sys.argv[1]
    with open(path) as file:
        grades = json.loads(file.read())
    admitted = []  # NOTE: using a list to hold collection of admitted students
    for candidate, scores in grades.items():
        grade = get_overall_grade(scores)
        chance = admit_chance(grade[2])  # NOTE: indexing tuples
        if chance.lower() != "low":
            # also valid: chance == "high" or chance == "moderate"
            admitted.append(candidate)
    print(admitted)

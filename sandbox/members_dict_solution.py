#! /usr/bin/env python3
"""making a collection of admitted candidates and their scores"""

import json
import sys

from score_calculator import get_overall_grade
from club_19052 import admit_chance

if __name__ == "__main__":
    path = sys.argv[1]
    with open(path) as file:
        grades = json.loads(file.read())
    admitted = {}  # NOTE: empty dictionary
    for candidate, scores in grades.items():
        grade = get_overall_grade(scores)
        chance = admit_chance(grade[2])
        # TODO unless chance is "low", the candidate should be admitted
        if chance.lower() != "low":
            # TODO candidates should be stored alongside their GPAs
            admitted[candidate] = grade[2]
    print(admitted)

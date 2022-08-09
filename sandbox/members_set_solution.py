#! /usr/bin/env python3
"""get a unique unordered collection of admitted candidates"""
import json
import sys
from copy import deepcopy

from score_calculator import get_overall_grade
from club_19052 import admit_chance

if __name__ == "__main__":
    path = sys.argv[1]
    with open(path) as file:
        grades = json.loads(file.read())
    grades = list(grades.items())
    # NOTE: this duplicates the last 2 records
    grades.extend(deepcopy(grades[-2:]))
    admitted = set()  # NOTE: using a set to avoid duplication
    for candidate, scores in grades:
        grade = get_overall_grade(scores)
        chance = admit_chance(grade[2])
        # TODO unless chance is "low", the candidate should be admitted
        if chance.lower() != "low":
            # NOTE: the use of string method lower is preferred, to have case
            # insensitive comparison
            # TODO make sure there are no duplication in our collection
            admitted.add(candidate)
    print(*admitted)

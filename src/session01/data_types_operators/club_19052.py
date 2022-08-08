#! /usr/bin/env python3
"""script to determine admission status for club 19052
"""
import json
import random
import sys

from .score_calculator import get_overall_grade

random.seed(42)


def admit_chance(gpa: float) -> str:
    """Tells the chances of a certain candidate on a 3-level scale:
        high, moderate, low
    A GPA of 1.3 or lower -> low chances
    GPA higher than 1.3 but at most 2.7 -> moderate
    GPA higher than 2.7 -> high
    """
    # TODO turn the rules to code
    if gpa <= 1.3: return "low"
    elif gpa <= 2.7: return "moderate"
    else: return "high" 

if __name__ == "__main__":
    path = sys.argv[1]
    with open(path) as file:
        grades = json.loads(file.read())
    # key, value = random.choice(list(grades.items()))
    key, value = list(grades.items())[2]
    grade = get_overall_grade(value)
    chance = admit_chance(grade[2])
    print(f"{key}'s chances are", chance)

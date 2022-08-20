#! /usr/bin/env python3
"""Custom utilities to demonstrate importing packages for local usage"""


def get_subject_overall_performance(grades: dict, subject: str) -> float:
    """finds the overall performance on a given subject

    Parameters
    ----------
    grades: dict

    subject: str

    Returns
    -------
    out: float

    Throws
    ------
    KeyError
    """
    performance = 0
    for marks in grades.values():
        # TODO: an exception could occur here
        performance += marks[subject]["score"]
    full_mark = list(grades.values())[0][subject]["mark"]
    return performance / (full_mark * len(grades))

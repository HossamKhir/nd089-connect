#! /usr/bin/env python3
"""Exercise on exception handling w/ try/except"""

# TODO: we are working w/ a json file, we need something from builtin library
# for just that
# TODO: we'd need some pre-defined functionality from another script `utils.py`


if __name__ == "__main__":
    path = input("Please, insert the path to the grades JSON file:\v")
    grades_file = open(path)
    # TODO: could have exceptions here, let's fix that
    grades_dict = json.load(grades_file)
    grades_file.close()
    math_performance = get_subject_overall_performance(grades_dict, "math")

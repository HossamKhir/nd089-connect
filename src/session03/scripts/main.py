#! /usr/bin/env python3
"""Exercise on exception handling w/ try/except"""

# TODO: we are working w/ a json file, we need something from builtin library
# for just that
import json
# import numpy as np # `as` keyword makes an alias
# TODO: we'd need some pre-defined functionality from another script `utils.py`
# import utils.get_subject_overall_performance
from utils import get_subject_overall_performance

from scripts.submod import PI

if __name__ == "__main__":
    prompt = "Please, insert the path to the grades JSON file:\v"
    path = input(prompt)
    prompt = "Please, state the subject:\t"
    subject = input(prompt)
    try:
        grades_file = open(path)
        # TODO: could have exceptions here, let's fix that
        grades_dict = json.load(grades_file) # loads
        grades_file.close()
        performance = get_subject_overall_performance(grades_dict, subject)
        print(f"performance of {subject} is {performance}")
    except json.decoder.JSONDecodeError as jde:
        print("this is not a json file")
    except FileNotFoundError as fnfe:
        print(f"File was not found\n{fnfe}")
    except Exception as e: # a good practice from PEP-8
        print("some error occurred")
    finally:
        print("thanks for using our script")
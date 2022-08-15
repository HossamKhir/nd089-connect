#! /usr/bin/env python3
"""notes on enumerate and zip functions"""

import random
import sys

random.seed(42)


if __name__ == "__main__":
    n = sys.argv[1] if len(sys.argv) > 2 else 8
    test_list = list(map(int, [10 * random.random() for _ in range(n)]))
    for i, val in enumerate(test_list):
        print(f"at index {i} we have {val}")
    double = [2 * i for i in test_list]
    squares = [i ** 2 for i in test_list]
    for el, dbl, sq in zip(test_list, double, squares):
        print(f"2x{el} is {dbl}\t{el}^2 is {sq}")

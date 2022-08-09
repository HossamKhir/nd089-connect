#! /usr/bin/env python3
"""Simple calculator for arithmetic operations

PEMDAS

"""
from __future__ import annotations

import sys


def main(op1: float | int, op2: float | int, operator: str) -> float | int:
    """the main function for the arithmetic calculator

    PEMDAS

    Parameters
    ----------
    op1: int, float
        the first operand
    op2: int, float
        the second operand
    operator: str
        string represents the operation requested

    Returns
    -------
    out: int, float
        the result of applying the requested operation on the operators
    """
    res = 0  # assignment operator
    if operator == "**" or operator == "^":
        pass  # TODO: implement exponentiation
    elif operator == "*":
        pass  # TODO: implement multiplication
    elif operator == "/" and op2:
        pass  # TODO: implement division
    elif operator == "//" and op2:
        pass  # TODO: implement integer division
    elif operator == "%" and op2:
        pass  # TODO: implement modulus
    elif operator == "+":
        pass  # TODO: implement addition
    elif operator == "-":
        pass  # TODO: implement subtraction

    return res


if __name__ == "__main__":
    op1, operator, op2 = sys.argv[1:]
    result = main(op1, op2, operator)
    print(*sys.argv[1:], "=", result)

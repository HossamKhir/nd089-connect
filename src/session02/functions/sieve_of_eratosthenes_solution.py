#! /usr/bin/env python3
"""exercise on control flow + data structures"""

from argparse import ArgumentParser, Namespace
from math import ceil, sqrt


def get_args() -> Namespace:
    """Utility method to retrieve command line arguments

    Returns
    -------
    out: argparse.Namespace
        the argparse namespace that holds arguments
    """
    args = ArgumentParser()
    _ = args.add_argument(
        "-s",
        action="store",
        type=int,
        default=0,
        help="the starting index",
        dest="start",
    )
    _ = args.add_argument("end", action="store", type=int, help="the ending index")
    return args.parse_args()


def get_primes(end: int, start: int = 2) -> list:
    """Using sieve of eratosthenes to find primes

    Parameters
    ----------
    end: int
        the ending index to look for primes less than it
    start: int
        the starting index to look for primes, if `None`, defaults to $2$

    Returns
    -------
    out: list
        list of primes less or equal to `end`
    """
    sieve = list(range(end + 1))
    i = 2
    while i * i <= end:
        if sieve[i]:
            for j in range(i * i, end + 1, i):
                sieve[j] = 0
        i += 1

    return sorted(set(sieve))[1:][start:]


def get_primes_forloop(end, start: int = 0) -> list:
    """Using sieve of eratosthenes to find primes

    Parameters
    ----------
    end: int
        the ending index to look for primes less than it
    start: int
        the starting index to look for primes, if `None`, defaults to $2$

    Returns
    -------
    out: list
        list of primes less or equal to `end`
    """
    sieve = [*range(2, end + 1)]
    for i in range(2, ceil(sqrt(end))):
        if sieve[i - 2]:
            for j in range((i * i) - 2, len(sieve), i):
                sieve[j] = 0

    return [i for i in sieve[start:] if i]


if __name__ == "__main__":
    args = get_args()
    primes = get_primes(start=args.start, end=args.end)
    # primes = get_primes_forloop(start=args.start, end=args.end)
    print(f"primes between {args.start} and {args.end} are:\n{primes}")

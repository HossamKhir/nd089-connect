#! /usr/bin/env python3
"""exercise on control flow + data structures"""

from argparse import ArgumentParser, Namespace


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
    # TODO implement sieve of eratosthenes

    # NOTE regardless of the start index sent, the sieve always starts at 2
    # TODO select a proper ordered data structure, and fill it with values until
    # the given end index

    # TODO use indices to cover the data structure's values until sqrt(end)
    #   TODO if the index has value:
    #       TODO zero-out multiples of that value till end

    # TODO return the primes from start (inclusive) till end (inclusive)
    return None


if __name__ == "__main__":
    args = get_args()
    primes = get_primes(start=args.start, end=args.end)
    print(f"primes between {args.start} and {args.end} are:\n{primes}")

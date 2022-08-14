#! /usr/bin/env python3
"""exercise on control flow + data structures"""

from argparse import ArgumentParser

if __name__ == "__main__":
    # receive command line arguments
    parser = ArgumentParser()
    _ = parser.add_argument(
        "-s",
        action="store",
        type=int,
        default=0,
        help="the starting index",
        dest="start",
    )
    _ = parser.add_argument("end", action="store", type=int, help="the ending index")
    args = parser.parse_args()

    start = args.start
    end = args.end

    # TODO implement sieve of eratosthenes

    # NOTE regardless of the start index sent, the sieve always starts at 2
    # TODO select a proper ordered data structure, and fill it with values until
    # the given end index

    # TODO use indices to cover the data structure's values until sqrt(end)
    #   TODO if the index has value:
    #       TODO zero-out multiples of that value till end

    # TODO return the primes from start (inclusive) till end (inclusive)
    primes = None
    print(f"primes between {args.start} and {args.end} are:\n{primes}")

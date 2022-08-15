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

    # NOTE regardless of the start index sent, the sieve always starts at 2
    # NOTE we select list as it is an ordered mutable data structure
    sieve = [*range(end + 1)]  # thanks for Josue Magallanes
    # ALTERNATIVELY: sieve = list(range(end+1))
    # NOTE we use end+1 as range returns exclusive end index
    # NOTE I prefer using sieve starting at 0 to have both index and value hold
    #   the same value
    # sieve = [0, 1, 2, 3, 4, ...]
    # idx   = [0, 1, 2, 3, 4, ...]
    # if you decide to use sieve from 2 onward
    # sieve = [2, 3, 4, 5, ...]
    # idx   = [0, 1, 2, 3, ...]

    i = 2  # start indexing at 2 (otherwise, all numbers will end up non-prime)
    # NOTE if you select the sieve starting at 2 you may have 2 options
    # 1. use `i` as index (same approach), then use: i = 0
    # 2. use `i` as next number in sequence, then inside your loop, you'd need
    #   to compensate for the difference depicted in previous note
    while i * i <= end:
        # NOTE this is preferred way to loop across the sieve, while for will
        #   work, it is relatively easy to implement for in python, but not in
        #   other languages that doesn't provide a range function
        # NOTE if you'd like to use for:
        # for i in range(math.ceil(math.sqrt(end))): # don't tell you think
        #   this is prettier than the while way
        if sieve[i]:
            # NOTE in python (and some other programming language) booleans can
            #   be inferred from the absence of a value or not, in python
            #   anything that is not {0, None, False, "", {}, [], set()}, is
            #   coerced (translated) into false
            for j in range(i * i, end + 1, i):
                sieve[j] = 0  # we mark non-primes as being 0
        i += 1  # NOTE don't forget to alter the while conditional

    primes = sorted(set(sieve))[1:][start:]
    # ALTERNATIVELY: primes = [i for i in sieve[start:] if i]
    # NOTE you may filter inside a comprehension statement, by appending the
    #   conditional to the end
    # [
    # i for i in iterable
    # if satisfy_condition(i)
    # ]
    print(f"primes between {args.start} and {args.end} are:\n{primes}")
    # NOTE under the ../functions/sieve_of_eratosthenes_solution.py, we touch
    #   on the power of functions, and we implement all shapes of this algorithm
    #  (the ones inside comments)

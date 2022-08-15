#! /usr/bin/env python3
"""simple emulation of the game nim"""
import random
import sys


def play_nim(sticks: int = 7) -> str:
    """plays nim, and determines the winner

    Parameters
    ----------
    sticks: int
        the number of sticks available

    Returns
    -------
    out: str
        a string depicting who won
    """
    print(f"sticks:\t{sticks}")
    player = 0  # 0 is the player, 1 is the computer

    while sticks:
        if player:
            print("computer turn")
            if sticks == 1:
                player ^= 1
                break
            elif sticks in range(2, 5):
                sticks = 1
            else:
                sticks -= random.choice([1, 2, 3])
        else:
            opts = list(range(1, min(3, sticks) + 1))
            remove = int(input(f"Select from: {opts}:\t"))
            if remove not in opts:
                print("invalid selection")
                continue
            sticks -= remove
        player ^= 1
        print(f"sticks:\t{sticks}")

    return "I" if player else "U"


if __name__ == "__main__":
    winner = play_nim(int(sys.argv[1]) if len(sys.argv) >= 2 else 7)
    print(f"{winner} Won!!!")

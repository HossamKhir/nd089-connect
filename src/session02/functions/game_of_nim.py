#! /usr/bin/env python3
"""simple emulation of the game nim"""
import sys


def play_nim(sticks: int = 7):
    """plays nim, and determines the winner"""
    # TODO the game should continue until there are no sticks left

    # TODO this is a 2 player game, so turns should be taken
    # TODO if it is computer's turn
    #   TODO sticks: pick -> 4:3, 3:2, 2|1:1, 5+:random(1,2,3)
    # TODO if it is user's turn
    #   TODO check if user picks no more than 3, if available

    # TODO the last player to pick lost
    return ""


if __name__ == "__main__":
    winner = play_nim(sys.argv[1] if len(sys.argv) > 2 else 7)
    print(f"{winner} Won!!!")

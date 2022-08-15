#! /usr/bin/env python3
"""simple emulation of the game nim"""
import random
import sys

random.seed(42)

if __name__ == "__main__":
    sticks = int(sys.argv[1]) if len(sys.argv) >= 2 else 7
    print(f"sticks:\t{sticks}")
    player = 0  # 0 is the player, 1 is the computer

    # NOTE since this game should repeat steps until some condition is met, a
    #   while loop is best
    while sticks:  # since sticks is an `int`, it should be false only when it
        # reaches 0
        if player:
            print("computer turn")
            if sticks == 4:
                sticks -= 3
            elif sticks == 3:
                sticks -= 2
            elif sticks <= 2:
                sticks -= 1
            else:
                sticks -= random.choice([1, 2, 3])
            # ALTERNATIVELY:
            # if sticks == 1:
            #     player ^= 1
            #     break
            # elif sticks in range(2, 5):
            #     sticks = 1
            # else:
            #     sticks -= random.choice([1, 2, 3])
        else:
            opts = list(range(1, min(3, sticks) + 1))
            remove = int(input(f"Select from: {opts}:\t"))
            if remove not in opts:
                print("invalid selection")
                continue
            sticks -= remove
        # NOTE in binary operations, using XOR 1 flips the bit
        player ^= 1
        print(f"sticks:\t{sticks}")

    # TODO the last player to pick lost
    winner = "I" if player else "U"
    print(f"{winner} Won!!!")
    # NOTE don't forget to check ../functions/game_of_nim_solution.py

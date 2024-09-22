#!/usr/bin/env python3

# NOTE: THIS FILE IS WHAT YOU RUN TO PROGRESS THROUGH THE GAME.
#       Please DO NOT modify any file other than those in the `puzzles` folder
#       If the progress is tampered with, this file will reset the progress to

# ========== IMPORTS ==========

from internal.progress import read_progress, reset_progress, save_progress
from puzzles import part1, part2, aprt3

# ========== MAIN RUNNING SCRIPT ==========

def main():
    # Attempt to read what level the plater
    with open("progress.txt", "r") as f:
        hash: str = f.readline()

        level: int
        try:
            level: int = read_progress(hash)
        except ValueError as e:
            print(f"Error: {e}")
            print("Resetting progress...")
            reset_progress()
            level: int = 0

        if level == 0:
            print("hi0")
            save_progress(1)

        if level == 1:
            if part1.fizzbuzz():
                print("level one complete!")
                save_progress(2)

        if level > 1:
            print(f"hi{level}")
            save_progress(level + 1)

    return

if __name__ == "__main__":
    main()

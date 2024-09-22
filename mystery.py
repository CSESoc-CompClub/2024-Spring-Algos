#!/usr/bin/env python3

# NOTE: THIS FILE IS WHAT YOU RUN TO PROGRESS THROUGH THE GAME.
#       Please DO NOT modify any file other than those in the `puzzles` folder
#       If the progress is tampered with, this file will reset the progress to

# ========== IMPORTS ==========

from internal.autotesting.part1_test import (array_shift_test,
                                             fast_search_test, fizzbuzz_test,
                                             monthly_crime_test, search_test)
from internal.progress import read_progress, reset_progress, save_progress

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
            print("[storyline here]")
            save_progress(1)
            
        # =============================== Part 1 ===============================

        if level == 1:
            if fizzbuzz_test():
                save_progress(2)
        
        if level == 2:
            if array_shift_test():
                save_progress(3)
        
        if level == 3:
            if search_test():
                save_progress(4)
                
        if level == 4:
            if fast_search_test():
                save_progress(5)
        
        if level == 5:
            if monthly_crime_test():
                print("All part 1 questions have been completed!")
                print("[Storyline here]")
                save_progress(6)
        
        # =============================== Part 2 ===============================
        
        
        # =============================== Part 3 ===============================

    return

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import sys

# NOTE: THIS FILE IS WHAT YOU RUN TO PROGRESS THROUGH THE GAME.
#       Please DO NOT modify any file other than those in the `puzzles` folder
#       If the progress is tampered with, this file will reset the progress to

# ========== IMPORTS ==========
from internal.autotesting.generic_test import print_divider
from internal.autotesting.part1_test import (array_shift_test,
                                             fast_search_test, fizzbuzz_test,
                                             monthly_crime_test, search_test)
from internal.autotesting.part2_test import (is_palindrome_test,
                                             find_primes_test, has_combination_test,
                                             safe_cracking_test, max_items_test)
from internal.progress import read_progress, reset_progress, save_progress

# ========== MAIN RUNNING SCRIPT ==========

def main(test_level: (int | None)):
    if test_level != None:
        run_levels(int(test_level))
    else:
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
            
            print("Currently in debug mode. Run this file with the command python mystery.py [num]\nwhere [num] represents the number of the function you wish to test.")
            # commenting the below out for now to prevent people from accidentally progressing
            # run_levels(level)
    return

def run_levels(level: int):
    if level == 0:
        print_divider()
        print(
"""Welcome to your training!

Poco's needs to make sure you're suitable before you take on a case, so he's      
set up some functions for you to complete.

To start, go to puzzles/part1.py!!""")
        print_divider()
        save_progress(1)
        
    # =============================== Part 1 ===============================

    # Todo - implement hints?
    
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
            print(
"""All part 1 questions have been completed!

Generally a junior detective wouldn't be given a case this early in their career. 
However, Poco's confident in your abilities and he's giving you a chance 
to work on one directly!

Whilst you were completing your training exercises we managed to find Ob's safe, 
which we believe will contain significant clues to his whereabouts. 
The problem, however, is opening this safe. Thankfully, Ob's left us some hints.

We have a huge list of potential passwords, and now we need you to write functions 
that'll help to filter out which password is the right one. 
Note that the passwords are numerical and can be of any length.

Ob mentioned once to Poco that his passwords were palindromes since they were
easier to remember.

Proceed to puzzles/part2.py to begin!""")  
            print_divider()
            save_progress(6)
        
    # =============================== Part 2 ===============================
    
    if level == 6:
        if is_palindrome_test():
            print(
"""After digging through more of Ob's files, we've discovered another quirk of Ob's 
passwords; they contain prime numbers! However, we don't know what prime numbers 
just yet."""
            )
            
            print_divider()
            save_progress(7)
    
    if level == 7:
        if find_primes_test():
            print(
"""We're getting close to unlocking the safe now!

Poco found some of Ob's previous passwords and he's now realised that the 0s in a 
password is no coincidence. For example, the password 30193072 can also be represented 
in a list form: [3, 193, 72].

Poco believes the final property of the password is that two numbers in the array
form of a password must sum up to a given number."""
            )
            print_divider()
            save_progress(8)
    
    if level == 8:
        if has_combination_test():
            print(
"""Poco's finally narrowed down what the password could be, thanks to your help. 

We know that Ob's passwords:
   1. Are palindromes
   2. Contains the nth prime number the password's list form
   3. Contains two prime numbers that sum up to a given number in the password's 
      list form
   
Now it's time to sort through the list of potential passwords and see which one 
is the safe password!"""
            )
            print_divider()
            save_progress(9)
    
    if level == 9:
        if safe_cracking_test():
            print(
"""You successfully opened the safe and you look into to discover it ...empty?
Well, not quite. You realise that at the very back are two receipts.

From the first receipt, we can see that Ob had recently purchased a large number 
of items, to be shipped off to a censored location. The second receipt shows that
he arranged the items to be shipped off in multiple containers, since each container
has a maximum weight that it can hold.

We know the weight of all the items that Ob purchased, and we also know the
maximum capacity of each shipping container. Since different facilities have
different limits on how many items you can put in each shipping container, we 
now have a way to deduce Ob's general location."""
            )
            print_divider()
            save_progress(10)
    
    if level == 10:
        if max_items_test():
            print(
"""All part 2 questions have been completed!

Only one shipping company allows the calculated number of items per container; 
Locomotion Shipping. There's a high possibility that Ob could be at the company's 
item drop-off location, considering he still has some items left to ship.

Even if we don't find Ob, we've greatly narrowed down the area that Ob can be in, 
increasing our chances of success tenfold. Poco was right to put his faith in you.

Now, all that's left is to find Ob and find the cause of his disappeaerance. 

Continue to puzzles/part3.py to complete the case!
""")
            save_progress(11)
            
    # =============================== Part 3 ===============================

if __name__ == "__main__":
    # the second argument is for debugging purposes
    if (len(sys.argv) == 2):
        test_level = sys.argv[1]
    else:
        test_level = None
    main(test_level)

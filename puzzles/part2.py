from internal.provided import *
from puzzles.part1 import *

# Todo - move some of the story bloat to mystery.py + add a flag(?) that allows students to skip the story if they wish

# This is the second file intended to be completed. You may call any functions 
# you completed previously, whether it be in part 2 or part 1.

""" ------------------------------ Question 1 ------------------------------ """
# The location of Ob's safe has been identified, but now we have to crack it. 
# Unfortunately for us, Ob's safe password includes a combination of numbers and 
# letters, so our safe cracking efforts will need to be smart and efficient.
# 
# Ob mentioned once to Poco that his passwords were palindromes since they were
# easier to remember. As such, Poco's wants you to implement a function that 
# determines whether a given string is a palindrome.
#
# A palindrome is something that is the same backwards as it is forwards. For
# example, "racecar" is a palindrome. The function should return true if the string
# is a palindrome and false if not.
#
# Note that the string can include numbers, letters and other symbols.

def is_palindrome(string: str) -> bool:
    # Todo - complete this function!
    return None

""" ------------------------------ Question 2 ------------------------------ """
# After digging through more of Ob's files, we've discovered another quirk of 
# Ob's passwords. 

# possibilities of the safe - sieve
# TODO
def find_primes() -> int:
    return None

""" ------------------------------ Question 3 ------------------------------ """
# two sum but has to call find_primes
# TODO
def find_combination() -> int:
    return None

""" ------------------------------ Question 4 ------------------------------ """
# list rotation (can use part1 function)
# calls find_combination to determine how much to rotate list by and some other
# parv's algos go here
# TODO
def safe_cracking():
    # choose between palindrome, isogram or 
    return None

""" ------------------------------ Question 5 ------------------------------ """
# given a list of item where each slot represents the cost of the item and a budget,
# determine the maximum amount of items that can be bought with the budget
# [some storyline things here]
# TODO
def max_buy(costs: list[int], budget: int) -> int:
    return None

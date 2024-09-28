# Note: ALl but 2 test cases will be visible to students in part 2.

# ==============================================================================
# =================================== IMPORTS ==================================
# ==============================================================================

from puzzles.part2  import *
from solutions.part2_sol import *
from internal.autotesting.generic_test import *

# ==============================================================================
# ================================= QUESTION 6 =================================
# ==============================================================================

def is_palindrome_test() -> bool:
    name = "is_palindrome"
    
    # Check if the student implemented the function
    if not implemented_test(is_palindrome(0), name):
        return False
    
    # Todo - internals
    # The last 2 test cases should be hidden
    tests = []
    
    return passed_test(name, Qid[name])

# ==============================================================================
# ================================= QUESTION 7 =================================
# ==============================================================================

def find_primes_test() -> bool:
    name = "find_primes"
    
    # Check if the student implemented the function
    if not implemented_test(find_primes(1), name):
        return False
    
    # Todo - internals
    tests = []
    
    return passed_test(name, Qid[name])

# ==============================================================================
# ================================= QUESTION 8 =================================
# ==============================================================================

def has_combination_test() -> bool:
    name = "has_combination"
    
    # Check if the student implemented the function
    if not implemented_test(has_combination(101, 1), name):
        return False
    
    # Todo - internals
    tests = []
    
    return passed_test(name, Qid[name])

# ==============================================================================
# ================================= QUESTION 9 =================================
# ==============================================================================

def safe_cracking_test() -> bool:
    name = "safe_cracking"
    
    # Check if the student implemented the function
    if not implemented_test(safe_cracking([101,111], 1, 1), name):
        return False
    
    # Todo - internals
    tests = []
    
    return passed_test(name, Qid[name])

# ==============================================================================
# ================================= QUESTION 10 ================================
# ==============================================================================

def max_items_test() -> bool:
    name = "max_items"
    
    # Check if the student implemented the function
    if not implemented_test(max_items([],1), name):
        return False
    
    # Todo - internals
    tests = []
    
    return passed_test(name, Qid[name])


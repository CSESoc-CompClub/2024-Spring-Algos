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
    tests = [1, 11, 121, 1221, 13, 31, 12321, 123321, 1232, 2321, 123, 0]
    test_sols = [True, True, True, True, False, False, True, True, False, False, False, True]
    
    # Iterate over the tests and compare student's solution with our solution
    for i, test in enumerate(tests):
        student = is_palindrome(test)
        if (student != test_sols[i]):
            print(f"Test case {i} with n = {test} failed.")
            return compare_test(student, test_sols[i])
        else:
            print(f"Test case {i} passed!")

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
    tests = [1, 2, 3, 4, 5, 10, 20, 30, 40, 99]
    test_sols = [2, 3, 5, 7, 11, 29, 71, 113, 173, 523]

    for i, test in enumerate(tests):
        student = find_primes(test)
        if (student != test_sols[i]):
            print(f"Test case {i} with n = {test} failed.")
            return compare_test(student, test_sols[i])
        else:
            print(f"Test case {i} passed!")
    
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
    tests = [(10203, 4), (10203, 5), (10203, 6), (10203, 7), (15035055, 50), (15035055, 60), (12304560789, 579), (12304560789, 912), (12304560789, 1245), (12304560789, 123), (12304560789, 456), (12304560789, 789), (101010101, 5), (102030405, 9), (1011011101111011111, 12345), (1011011101111011111, 11122), (10203040506, 1)]
    test_sols = [True, True, False, False, True, False, True, True, True, False, False, False, False, True, False, True, False]

    for i, test in enumerate(tests):
        student = has_combination(test[0], test[1])
        solution = test_sols[i]
        if (student != solution):
            print(f"Test case {i} with n = {test} failed.")
            return compare_test(student, solution)
        else:
            print(f"Test case {i} passed!")
    
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
    tests = [([20302], 2, 5), ([20305], 2, 5), ([20302], 3, 5), ([20302], 2, 6), ([20302, 20305], 2, 5), ([20305, 20302], 2, 5), ([305070503, 13015017071051031, 2030405040302], 6, 46), ([20305, 20306], 2, 5), ([3050709011, 13015017071051031, 1012], 3, 13)]
    test_sols = [20302, 0, 0, 0, 20302, 20302, 13015017071051031, 0, 0]
    
    for i, test in enumerate(tests):
        student = safe_cracking(test[0], test[1], test[2])
        solution = test_sols[i]
        if (student != solution):
            print(f"Test case {i} with n = {test} failed.")
            return compare_test(student, solution)
        else:
            print(f"Test case {i} passed!")

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


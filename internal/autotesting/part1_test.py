# Note: ALl test cases will be visible to students in part 1.

# ==============================================================================
# =================================== IMPORTS ==================================
# ==============================================================================

from puzzles.part1  import *
from solutions.part1_sol import *
from internal.autotesting.generic_test import *

# ==============================================================================
# ================================= QUESTION 1 =================================
# ==============================================================================

def fizzbuzz_test() -> bool:
    name = "fizzbuzz"
    
    # Check if the student implemented the function
    if not implemented_test(fizzbuzz(0), name):
        return False

    # List of tests
    tests = [18, 0, 1, 100, 9999]

    # Iterate over the tests and compare student's solution with our solution
    for i, test in enumerate(tests):
        student = fizzbuzz(test)
        solution = fizzbuzz_sol(test)
        if (student != solution):
            print(f"Test case {i} with n = {test} failed.")
            return compare_test(student, solution)
        else:
            print(f"Test case {i} passed!")
    return passed_test(name, 1)

# ==============================================================================
# ================================= QUESTION 2 =================================
# ==============================================================================

def array_shift_test() -> bool:
    name = "array_shift"
    
    # Check if the student implemented the function
    if not implemented_test(array_shift([],0), name):
        return False
    
    # List of tests
    tests = [[[1,2,3,4],3], [[1],2], [[],4], [[4,8,2,3],9], [[0,1,2,3,4,5,6,7,8,9],50]]
    for i, test in enumerate(tests):
        student = array_shift(test[0], test[1])
        solution = array_shift_sol(test[0], test[1])
        if (student != solution):
            print(f"Test case {i} with arr = {test[0]} & n = {test[1]} failed.")
            return compare_test(student, solution)
        else:
            print(f"Test case {i} passed!")
    
    return passed_test(name, 2)

# ==============================================================================
# ================================= QUESTION 3 =================================
# ==============================================================================

def search_test() -> bool:
    name = "search"
    
    # Check if the student implemented the function
    if not implemented_test(search([],0), name):
        return False
    
    # TODO - internals: complete this
    tests = []
    
    return passed_test(name, 3)

# ==============================================================================
# ================================= QUESTION 4 =================================
# ==============================================================================

# returns whether the search function written by the student passed
# the time limit (True if passed, False if not passed)
def timer(func) -> bool:
    # TODO - dev: implement this
    # If time > 3 seconds, fail the test
    pass

def fast_search_test() -> bool:
    name = "fast_search"    
    
    # Check if the student implemented the function
    if not implemented_test(fast_search([],0), name):
        return False
    
    # TODO - dev: add 2 LARGE tests case (with and without targets) to make sure the student stays under the 3 second time limit
    # feel free to modify the below however you see fit to get things to work
    tests = [[[1,2,3,4,5],5], [[1,2,3,4,5],6], [[],1], "large test with target", "large test without target"]
    for i, test in enumerate(tests):
        if not timer(test):
            print(f"Your {name} function took over 3 seconds! Test failed.")
            return False 
        else:
            print(f"Test case {i} passed!")
    
    return passed_test(name, 4)


# ==============================================================================
# ================================= QUESTION 5 =================================
# ==============================================================================

def monthly_crime_test() -> bool:
    name = "monthly_crime"
    
    # Check if the student implemented the function
    if not implemented_test(monthly_crime([]), name):
        return False
    
    # TODO - internals: complete this
    tests = []
    
    return passed_test(name, 5)
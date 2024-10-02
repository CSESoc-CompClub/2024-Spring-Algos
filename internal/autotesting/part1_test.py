# ==============================================================================
# =================================== IMPORTS ==================================
# ==============================================================================

from puzzles.part1  import *
from solutions.part1_sol import *
from internal.autotesting.generic_test import *
from puzzles.part1  import *
from solutions.part1_sol import *
from internal.autotesting.generic_test import *
from typing import Callable
from enum import Enum
import random
import timeit

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
    return passed_test(name, Qid[name])

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
    
    return passed_test(name, Qid[name])

# ==============================================================================
# ================================= QUESTION 3 =================================
# ==============================================================================

def search_test() -> bool:
    name = "search"
    
    # Check if the student implemented the function
    if not implemented_test(search([],0), name):
        return False
    
    tests = [
        [[2, 3, 5, 1, 4], 5, 2],
        [[2, 3, 5, 1, 4], 6, -1],
        [[7, 3, 5, 1, 4], 7, 0],
        [[2, 3, 5, 1, 4], 4, 4],
        [[], 3, -1],
        [[3], 3, 0],
        [[2], 3, -1]
    ]
    
    for i, test in enumerate(tests):
        student = search(test[0], test[1])
        solution = test[2]
        if student != solution:
            print(f"Test case {i} with files = {test[0]} & target = {test[1]} failed.")
            return compare_test(student, solution)
        else:
            print(f"Test case {i} passed!")
    
    return passed_test(name, Qid[name])

# ==============================================================================
# ================================= QUESTION 4 =================================
# ==============================================================================

def fast_search_test() -> bool:
    name = "fast_search"    
    
    # Check if the student implemented the function
    if not implemented_test(fast_search([],0), name):
        return False
    
    print("Testing will take a few seconds!")
    
    arr_length = 5_000_000
    arr = random.sample(range(1, arr_length + 1), arr_length)
    arr.sort()
    
    test1_target = random.choice(arr)
    tests = [[arr, test1_target, arr.index(test1_target)], [arr, -1, -1], [[], 1, -1]]
    
    for i, test in enumerate(tests):
        [files, target, expected] = test
        
        start_time = timeit.default_timer()
        res = fast_search(files, target)
        
        if timeit.default_timer() - start_time > 0.1:
            print(f"Your {name} function took over 0.1 seconds! Test failed.")
            return False
        elif res != expected:
            print(f"Your {name} function returned the incorrect result! Test failed.")
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
    
    tests = [
        [[1, -1, 5, 1, -3, 0, 1, -1, -3, 1, 3, 4], [1,3,4]],
        [[], []],
        [[4], [4]],
        [[-4], [-4]],
        [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]],
        [[-3, -5, -2, -8, -6], [-2]],
        [[-2,1,-3,4,-1,2,1,-5,4], [4,-1,2,1]],
    ]

    for i, test in enumerate(tests):
        student = monthly_crime(test[0])
        solution = test[1]
        if student != solution:
            print(f"Test case {i} with array = {test[0]} failed.")
            return compare_test(student, solution)
        else:
            print(f"Test case {i} passed!")
    
    return passed_test(name, Qid[name])
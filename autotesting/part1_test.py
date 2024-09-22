# none of this works and i dont know why :sob:
import sys
sys.path.append("../2024-Spring-Algos")
from ..puzzles.part1  import *
from ..solutions.part1_sol import *

# All tests in part 1 will be visible

def implemented_test(result: any, func: str) -> bool:
    if (result == None):
        print(f"{func} not implemented.")
        return False
    return True

def fizzbuzz_test():  
    print("-------Testing fizzbuzz-------")
    # Check if the student implemented the function
    if not implemented_test(fizzbuzz(0), "Fizzbuzz"):
        return
    
    # List of tests
    tests = [18, 0, 1, 100, 9999]
    
    # Iterate over the tests and compare student's solution with our solution
    for i, test in enumerate(tests):
        student = fizzbuzz(test)
        solution = fizzbuzz_sol(test)
        if (student != solution):
            print(f"Test case {i} failed.")
            print(f"Your output: {student}")
            print(f"Expected output: {solution}")
            exit()
        else:
            print(f"Test case {i} passed!")

fizzbuzz_test()

def array_shift_test():
    result = array_shift()
    implemented_test(result, "Array shift")
    return None

def search_test(files: list[int], file_to_find: int):
    result = search_test()

def fast_search_test(files: list[int], file_to_find: int):
    result = fast_search()

def monthly_crime_test(crime_rates: list[int]):
    result = monthly_crime()
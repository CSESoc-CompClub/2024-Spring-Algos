# ==============================================================================
# =================================== IMPORTS ==================================
# ==============================================================================

from puzzles.part3 import *
from solutions.part3_sol import *
from internal.autotesting.generic_test import *

# ==============================================================================
# ================================= QUESTION 11 =================================
# ==============================================================================


def coin_change_test() -> bool:
    name = "coin_change"

    # Check if the student implemented the function
    if not implemented_test(coin_change([], 0), name):
        return False

    # Todo - internals
    # ALl test cases that aren't the provided ones should be hidden
    tests = [([1, 2, 5], 11), ([2], 3), ([1], 0)]

    test_sols = [3, -1, 0]

    # Iterate over the tests and compare student's solution with our solution
    for i, (coins, amount) in enumerate(tests):
        student = coin_change(coins, amount)
        if student != test_sols[i]:
            print(f"Test case {i} with coins = {coins} and amount = {amount} failed.")
            return compare_test(student, test_sols[i])
        else:
            print(f"Test case {i} passed!")

    # Hidden test cases
    hidden_tests = [
        ([], 0),
        ([0], 1),
        ([1, 3, 4], 6),
        ([2, 5, 10], 18),
        ([2, 3, 5], 7),
        ([5, 6], 8),
        ([1, 2], 2),
        ([1, 7], 3)([1, 5, 10, 25], 30),
        ([1, 2, 3], 7),
    ]

    hidden_sols = [-1, -1, 2, -1, 2, -1, 1, 3, 2, 3]

    for i, (coins, amount) in enumerate(hidden_tests):
        student = coin_change(coins, amount)
        if student != hidden_sols[i]:
            print(f"Hidden Test case {i} failed.")
            return compare_test(student, hidden_sols[i])
        else:
            print(f"Hidden Test case {i} passed!")

    return passed_test(name, Qid[name])

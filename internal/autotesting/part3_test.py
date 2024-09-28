# ==============================================================================
# =================================== IMPORTS ==================================
# ==============================================================================

from puzzles.part3  import *
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
    tests = []
    
    return passed_test(name, Qid[name])
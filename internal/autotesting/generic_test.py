# Question IDs
Qid = {
    "fizzbuzz": 1,
    "array_shift": 2,
    "search": 3,
    "fast_search": 4,
    "monthly_crime": 5,
    "is_palindrome": 6,
    "find_primes": 7,
    "has_combination": 8,
    "safe_cracking": 9,
    "max_items": 10
}

def print_divider():
    print("================================================================================")

def implemented_test(result: any, func: str) -> bool:
    print_divider()
    print(f"------- Testing {func} -------")
    if (result == None):
        print(f"{func} not implemented.")
        print_divider()
        return False
    print_divider()
    return True

def compare_test(student: any, solution: any) -> bool:
    print(f"Your output: {student}")
    print(f"Expected output: {solution}")
    return False
    
def passed_test(name: str, num: int) -> bool:
    print(f"All tests passed. Question {num} ({name}) complete!")
    print_divider()
    return True
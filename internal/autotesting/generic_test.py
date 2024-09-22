def implemented_test(result: any, func: str) -> bool:
    print(f"-------Testing {func}-------")
    if (result == None):
        print(f"{func} not implemented.")
        return False
    return True

def compare_test(student: any, solution: any) -> bool:
    print(f"Your output: {student}")
    print(f"Expected output: {solution}")
    return False
    
def passed_test(name: str, num: int) -> bool:
    print(f"All tests passed. Question {num} ({name}) complete!")
    return True
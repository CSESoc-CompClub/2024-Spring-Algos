from internal.provided import *
def fizzbuzz_sol(n: int) -> list[str]:
    a = []
    for i in range(n):
        if ((i % 3 == 0 or i % 5 == 0) and not (i % 3 == 0 and i % 5 == 0)):
            a.append(i)
    return a

def array_shift_sol(arr: list[int], k: int) -> list[int]:
    k = k % len(arr)
    return arr[k-1:] + arr[:k-1]

def search_sol(files: list[int], file_to_find: int) -> int:
    return linear_search(files)

def fast_search_sol(files: list[int], file_to_find: int) -> int:
    files.sort()
    return binary_search(files)

def monthly_crime_sol(crimeRates: list[int]) -> list[int]:
    return max_subarray(crimeRates)
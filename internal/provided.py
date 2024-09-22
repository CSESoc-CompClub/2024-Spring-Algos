# This files contains all the provided functions that were discussed in the lecture
# and are also listed on the cheatsheet. You are encouraged to use any of these 
# functions to help you solve the questions in part1.py, part2.py and part3.py

# Linear search. Returns the index of the target if found, and -1 if not found.
def linear_search(nums: list[int], target: int) -> int:
    for i, n in enumerate(nums):
        if n == target:
            return i

    return -1 # Target not found

# Binary search. Returns the index of the target if found, and -1 if not found.
def binary_search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1 # Target not found

# Modified Kadane's Algorithm. Returns the maximum subarray of a given array.
def max_subarray(arr: list[int]) -> list[int]: 
    max_so_far = 0
    current_max = 0
    start_index = 0
    end_index = 0
    j = 0

    for i in range(len(arr)):
        current_max += arr[i]

        if current_max > max_so_far:
            max_so_far = current_max
            start_index = j
            end_index = i

        if current_max < 0:
            current_max = 0
            j = i + 1

    result_array = arr[start_index: end_index + 1]
    return result_array
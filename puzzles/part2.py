from internal.provided import generate_primes, print_primes

# This is the second file intended to be completed.

""" ------------------------------ Question 6 ------------------------------ """
# Poco's wants you to implement a function that determines whether a given number is a palindrome.
#
# A palindrome is something that is the same backwards as it is forwards.
#
# For example, "12321" is a palindrome. The function should return true if the number
# is a palindrome and false if not.
#
# Assumptions:
#   Password wil be provided


def is_palindrome(password: int) -> bool:
    # Todo - complete this function!
    return None


""" ------------------------------ Question 7 ------------------------------ """
# Now Poco needs you to write an algorithm that'll return the nth prime number.
#
# As an example, if n = 4, find_primes would return 7 as it is the fourth prime
# number since you have [2,3,4,7]
#
# Note: the 100th prime is 541.
#
# Assumptions:
#   0 < n < 100


def find_primes(n: int) -> int:
    # Todo - complete this function!
    return None


""" ------------------------------ Question 8 ------------------------------ """
# You are required to implement the function has_combation, which will return true
# if there are two numbers in the list form of password that sum up to n,
# and false if otherwise.
#
# For example, if you were given password = 30193072 and n = 75, you would first
# convert 30193072 into [3, 193, 72] then there would be two numbers 72 and 3
# that sum up to 75, so has_combination would return true.
#
# Alternatively, if n = 76, then there are no two numbers in the list [3, 193, 72]
# so has_combination will return false.
#
# Assumptions/restrictions:
#   You may not use the same element twice - e.g. if you have the list
#   [1, 2, 3] and n = 6, you cannot have 3+3 as a sum so has_combination
#   would return false.


def has_combination(password: int, n: int) -> bool:
    # Todo - complete this function!
    return None


""" ------------------------------ Question 9 ------------------------------ """
# We know that Ob's passwords:
#   1. Are palindromes
#   2. Contains the nth prime number the password's list form
#   3. Contains two numbers that sum up to a given number in the password's list form
#
# Example cases:
#   password = 3031202907, nth_prime = 4, prime_sum = 3
#     1. This is not a palindrome
#     2. The list form [3, 312, 29, 7] contains the 4th prime number 7
#     3. There are no two numbers that sum up to 3
#     This is not the password as it fails condition 1 & 3
#
#   password = 303101303, nth_prime = 3, prime_sum = 33
#     1. This is a palindrome
#     2. The list form [3, 31, 13, 3] does not contain the 3rd prime number 5
#     3. There are two numbers (31, 3) that sum up to 33
#     This is not the password as it fails condition 2
#
# Assumptions:
#   - There will always be only be one valid password in the passwords array


def safe_cracking(passwords: int, nth_prime: int, prime_sum: int) -> int:
    # Todo - complete this function!
    return None


""" ------------------------------ Question 10 ----------------------------- """
# You are to implement an algorithm that'll return the maximum amount of
# items a shipping container with k weight can hold.
#
# For example, items = [4, 7, 4, 3, 5], where each element representing the
# weight of an item. If weight = 13, then the maximum weight of the
# shipping container is 13. Therefore, max_items would return 3, since you
# can have items of weights 3, 4 and 4 which sums up to 11.
#
# Assumptions:
#   weight > 0


def max_items(items: list[int], weight: int) -> int:
    # Todo - complete this function!
    return None

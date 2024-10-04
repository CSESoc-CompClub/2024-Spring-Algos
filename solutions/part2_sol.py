from internal.provided import *


def is_palindrome_sol(password: int) -> bool:
    if str(password)[::-1] == str(password):
        return True
    return False


# find nth prime
def find_primes_sol(n: int) -> int:
    primes = generate_primes(541) # 541 is the 100th prime
    count = 0
    for num in primes:
        if num != 0:
            count += 1
        if count == n:
            return num


# two sum
def has_combination_sol(password: int, n: int) -> bool:
    # Convert password to list version
    list_pass = str(password).split("0")
    # Convert passwords back to integer form
    for i in range(len(list_pass)):
        list_pass[i] = int(list_pass[i])
    # Two sum
    for i in range(len(list_pass)):
        for j in range(i + 1, len(list_pass)):
            if list_pass[i] + list_pass[j] == n:
                return True
    return False


def safe_cracking_sol(passwords: int, nth_prime: int, prime_sum: int) -> int:
    for password in passwords:
        # must convert the password to its list form for find_primes to work
        # this is the same as what they did in has_combination
        list_pass = str(password).split("0")
        # Convert passwords back to integer form
        for i in range(len(list_pass)):
            list_pass[i] = int(list_pass[i])
        if (
            is_palindrome(password)
            and has_combination(password, prime_sum)
            and (find_primes(nth_prime) in list_pass)
        ):
            return password
    return 0 # this return 0 is not necessary since each autotest is guaranteed to have a valid password


def max_items_sol(items: list[int], weight: int) -> int:
    items.sort()
    total = 0
    bought = 0
    for i in range(len(items)):
        if total + items[i] <= weight:
            bought += 1
            total += items[i]
        else:
            return bought
    return bought

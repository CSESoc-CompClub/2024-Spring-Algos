from internal.provided import *

def is_palindrome_sol(password: int) -> bool:
    if (str(password)[::-1] == str(password)):
        return True
    return False

# find nth prime
def find_primes_sol(n: int) -> int:
    primes = generate_primes(100)
    count = 0
    for num in primes:
        if num != 0:
            count += 1
        if count == n:
            return num

# two sum
def has_combination_sol(password: int, n: int) -> bool:
    # Convert password to list version
    list_pass = str(password).split('0')
    for i in range(len(list_pass)):
        for j in range(i + 1, len(list_pass)):
            if list_pass[i] + list_pass[j] == n:
                return True
    return False

def safe_cracking_sol(passwords: int, nth_prime: int, prime_sum: int) -> int:
    for password in passwords:
        if is_palindrome_sol(password) and has_combination_sol(password, prime_sum) and (find_primes_sol(nth_prime) in password):
            return password
    return 0 #this is unnecessary for the student to implement but will be used here for debugging purposes

def max_items_sol(items: list[int], weight: int) -> int:
    items.sort()
    total = 0
    bought = 0
    for i in range(len(items)):
        if (total + items[i] <= weight):
            bought += 1
            total += items[i]
        else:
            return bought
    return bought

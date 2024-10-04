# Same as the leetcode problem
def coin_change_sol(coins: list[int], amount: int) -> int:
    # Special case: If there are no coins, then you cannot make up any amount
    if (len(coins) == 0):
        return -1
    
    # Initialize dp array with a large number (infinity)
    dp = [float('inf')] * (amount + 1)
    
    # Base case: 0 coins are needed to make amount 0
    dp[0] = 0

    # Loop over each coin in the list of coins
    for coin in coins:
        # Update the dp array for all amounts from coin to amount
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[amount] is still infinity, it means it's impossible to form the amount
    return dp[amount] if dp[amount] != float('inf') else -1

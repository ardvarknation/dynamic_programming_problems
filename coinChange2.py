# Solution for LeetCode problem "Coin Change" using Recursive + Memoization
# (Top-Down DP).

# Description:
#  You are given an integer array coins representing coins of different 
#  denominations and an integer amount representing a total amount of money.
#  Return the fewest number of coins that you need to make up that amount.
#  If that amount cannot be made up of any combination of the coins, return -1.
#  You may assume that have an infinite number of each kind of coin.

# Constraints:
# - 1 <= coins.length <= 12
# - 1 <= coins[i] <= 2^31 - 1
# - 0 <= amount <= 10^4

# Complexity:
# - Time: O(amount x len(coins))
# - Space: O(amount)

def coinChange(self, coins: list[int], amount: int) -> int:

  # Cache previously computed results
  memo = {}

  def dfs(remaining):
    # Base cases
    if remaining == 0:
      return 0

    if remaining < 0:
      return float('inf')

    # Return cached result if available
    if remaining in memo:
      return memo[remaining]

    min_coins = float('inf')

    # Try each coin
    for coin in coins:
      min_coins = min(
        min_coins,
        dfs(remaining - coin) + 1
      )

    # Store result
    memo[remaining] = min_coins

    return min_coins

  answer = dfs(amount)

  return answer if answer != float('inf') else -1
  

# Solution for LeetCode problem "Coin Change" using Bottom-Up DP.

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
  # Create a DP array where:
  # dp[i] = minimum number of coins needed to make amount i

  # Initialize all values to a number larger than any possible answer
  # (amount + 1 acts like "infinity")
  dp = [amount + 1] * (amount + 1)

  # Base case:
  # It takes 0 coins to make an amount of 0
  dp[0] = 0

  # Calculate the minimum number of coins needed for every amount from 
  # 1 up to target amount
  for current_amount in range(1, amount + 1):

    # Try using each coin denomination
    for coin in coins:

      # Only process if the coin is not larger than the current amount
      if coin <= current_amount:

        # If we use this coin, then:
        # 1 coin + the best solution for
        # (current_amount - coin)
        dp[current_amount] = min(
          dp[current_amount],
          dp[current_amount - coin] + 1
        )

  # If the value is still amount + 1, it means amount cannot be formed
  if dp[amount] == amount + 1:
    return -1

  return dp[amount]
  

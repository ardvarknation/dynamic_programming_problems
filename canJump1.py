# Solution 1 for LeetCode problem "Jump Game", using Bottom-Up (tabular)
# dynamic programming approach.

# Description:
#  You are given an integer array nums. You are initially positioned at
#  the array's first index, and each element in the array represents your
#  maximum jump length at that position.
#  Return True if the last index can be reached, or False otherwise.

# Constraints:
# - 1 <= nums.length <= 10^4
# - 0 <= nums[i] <= 10^5

# Complexity:
# - Time: O(n^2)
# - Space: O(n)

def canJump(self, nums: List[int]) -> bool:
  """
  Determines whether we can reach the last index.

  dp[i] = True if we can reach the last index starting from i.
  dp[i] = False otherwise.
  """

  n = len(nums)

  # Create a DP array initialised to False.
  dp = [False] * n

  # Base case:
  # We are already at the last index, so it is reachable.
  dp[n - 1] = True

  # Process positions from right to left.
  for i in range(n - 2, -1, -1):

    # Furthest position we can jump to from index i.
    furthest = min(i + nums[i], n - 1)

    # Check whether any reachable position can eventually 
    # reach the end.
    for j in range(i + 1, furthest + 1):

      if dp[j]:
        dp[i] = True
        break    # No need to check further.

  # Answer: Can we reach the last index from index 0?
  return dp[0]

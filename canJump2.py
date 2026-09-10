# Solution 2 for LeetCode problem "Jump Game", using Top-Down 
# (memoization) dynamic programming approach.

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
  Recursive DP solution with memoization.

  memo[i] stores whether index i can reach the last index.
  """
  n = len(nums)

  # Cache previously computed results.
  memo = {}

  def dfs(i):
    """
    Returns True if we can reach the end starting from index i.
    """

    # Base case:
    # Reached or passed the final index.
    if i >= n - 1:
      return True

    # Return cached answer if available.
    if i in memo:
      return memo[i]

    # Try every possible jump length.
    for step in range(1, nums[i] + 1):

      next_index = i + step

      # If any next position reaches the end, current
      # position is also successful. 
      if dfs(next_index):
        memo[i] = True
        return True

    # No jump worked.
    memo[i] = False
    return False

  return dfs(0)

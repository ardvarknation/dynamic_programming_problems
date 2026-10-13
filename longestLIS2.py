# Solution 2 using Recursive + Memoization DP approach 
# for LeetCode problem "Longest Increasing Subsequence".

# Description:
#   Given an integer array nums, return the length of the 
#   longest strictly increasing subsequence.

# Constraints:
# 1 <= nums.length <= 2500
# -10^4 <= nums[i] <= 10^4

# Complexity:
# O(n^2)

from functools import lru_cache

def lengthOfLIS(self, nums: list[int]) -> int:

  @lru_cache(None)
  def dfs(i):
    """
    Return the length of the LIS ending at index i.
    """
    best = 1

    for j in range(i):

      if nums[j] < nums[i]:
        best = max(best, dfs(j) + 1)

    return best

  return max(dfs(i) for i in range(len(nums)))

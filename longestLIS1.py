# Solution 1 using Classic DP approach for LeetCode problem "Longest Increasing Subsequence".

# Description:
#   Given an integer array nums, return the length of the longest strictly increasing subsequence.

# Constraints:
# 1 <= nums.length <= 2500
# -10^4 <= nums[i] <= 10^4

# Complexity:
# O(n^2)

def lengthOfLIS(self, nums: list[int]) -> int:
  """
  Returns the length of the longest increasing subsequence.

  dp[i] = length of the LIS ending at index i.
  """

  n = len(nums)

  # Every element by itself forms a subsequence of length 1.
  dp = [1] * n

  # Consider each position as the end of the subsequence.
  for i in range(n):

    # Look back at all previous elements.
    for j in range(i):

      # Can nums[i] extend the subsequence ending at j?
      if nums[j] < nums[i]:

        dp[i] = max(
          dp[i],
          dp[j] + 1
        )

  return max(dp)    

# Solution 3 using Patience Sorting algorithm (Optimal) 
# for LeetCode problem "Longest Increasing Subsequence".

# Description:
#   Given an integer array nums, return the length of the
#   longest strictly increasing subsequence.

# Constraints:
# 1 <= nums.length <= 2500
# -10^4 <= nums[i] <= 10^4

# Complexity:
# - Time: O(n^2)
# - Space: O(n)

from bisect import bisect_left

def lengthOfLIS(self, nums: list[int]) -> int:
  """
  Optimal solution. 

  tails[i] = smallest possible tail value
  for an increasing subsequence of length i + 1.
  """

  tails = []

  for num in nums:

    # Find where num belongs.
    pos = bisect_left(tails, num)

    # If num is larger than everything,
    # extend the longest subsequence.
    if pos == len(tails):
      tails.append(num)

    # Otherwise replace a larger tail.
    else:
      tails[pos] = num

  return len(tails)

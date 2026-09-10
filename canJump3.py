# Solution 3 for LeetCode problem "Jump Game", using Greedy approach.
# (Optimal solution, not strictly dynamic programming).

# Description:
#  You are given an integer array nums. You are initially positioned at
#  the array's first index, and each element in the array represents your
#  maximum jump length at that position.
#  Return True if the last index can be reached, or False otherwise.

# Constraints:
# - 1 <= nums.length <= 10^4
# - 0 <= nums[i] <= 10^5

# Complexity:
# - Time: O(n)
# - Space: O(1)

def canJump(self, nums: List[int]) -> bool:
  """
  Greedy approach.
  
  Tracks the leftmost position that can reach the end.
  """
  # Initially, the last index can reach itself.
  goal = len(nums) - 1

  # Work backwards through the array.
  for i in range(len(nums) - 2, -1, -1):

    # If we can jump from i to the current goal, then i
    # becomes the new goal.
    if i + nums[i] >= goal:
      goal = i

  # If goal became 0, we can reach the end.
  return goal == 0

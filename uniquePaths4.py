# Solution 4 for LeetCode problem "Unique Paths" using space-optimized DP.

# Description:
#  There is a robot on an m x n grid. The robot is initially located in the 
#  top-left corner (i.e. grid[0][0]). The robot tries to move to the bottom-
#  right corner (i.e. grid[m - 1][n - 1]). The robot can only move either
#  down or right at any point in time.
#  Given two integers, m and n, return the number of unique paths that the 
#  robot can take to reach the bottom-right corner.
#  The test cases are generated so that answer will be less than or equal to
#  2 * 10^9.

# Constraints:
# - 1 <= m, n <= 100

# Complexity:
# - Time: O(m * n)
# - Space: O(n)

def uniquePaths(self, m: int, n: int) -> int:

  # First row is all 1's.
  dp = [1] * n

  # Process remaining rows.
  for row in range(1, m):

    # Start from column 1 because column 0 
    # always stays 1.
    for col in range(1, n):

      # dp[col]     =  value from above
      # dp[col - 1]  =  value from the left
      dp[col] = dp[col] + dp[col - 1]

  return dp[-1]
      

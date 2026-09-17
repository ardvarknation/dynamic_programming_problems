# Solution 3 for LeetCode problem "Unique Paths" using Bottom-Up DP.

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
# - Space: O(m * n)

def uniquePaths(self, m: int, n: int) -> int:

  # Create an m x n grid.
  dp = [[0] * n for _ in range(m)]

  # First row only has one way to reach each cell.
  for col in range(n):
    dp[0][col] = 1

  # First col has only one way to reach each cell.
  for row in range(m):
    dp[row][0] = 1

  # Fill remaining cells.
  for row in range(1, m):
    for col in range(1, n):

      # Current cell can be reached from:
      # top + left.
      dp[row][col] = (
        dp[row - 1][col] +
        dp[row][col - 1]
      )

  return dp[m - 1][n - 1]

# Solution 2 for LeetCode problem "Unique Paths" using Recursion and Memoization -
# Top-Down DP.

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
  # Memo dictionary:
  # key = (row, col)
  # value = number of paths from that cell.
  memo = {}

  def dfs(row, col):

    # Reached destination.
    if row == m - 1 and col == n - 1:
      return 1

    # Outside grid.
    if row >= m or col >= n:
      return 0

    # Already solved this subproblem.
    if (row, col) in memo:
      return memo[(row, col)]

    # Compute answer.
    down = dfs(row + 1, col)
    right = dfs(row, col + 1)

    memo[(row, col)] = down + right

    return memo[(row, col)]

  return dfs(0, 0)
  

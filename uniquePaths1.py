# Solution 1 for LeetCode problem "Unique Paths" using brute-force recursion.

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
# - Time: O(2^(m+n))
# - Space: O(2^(m+n))

def uniquePaths(self, m: int, n: int) -> int:

  # Returns the number of unique paths from (row, col)
  # to the bottom-right corner.
  def dfs(row, col):

    # Reached destination.
    if row == m - 1 and col == n - 1:
      return 1

    # Outside grid.
    if row >= m or col >= n:
      return 0

    # Total paths = paths going down + paths going right.
    return dfs(row + 1, col) + dfs(row, col + 1)

  return dfs(0, 0)

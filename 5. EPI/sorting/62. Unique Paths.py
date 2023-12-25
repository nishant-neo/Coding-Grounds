"""
62. Unique Paths
Solved
Medium

Topics

Companies
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

Constraints:

1 <= m, n <= 100
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        ways = [[0 for i in range(n+1)] for _ in range(m+1)]

        for i in range(m+1):
            ways[i][0] = 1

        for i in range(n+1):
            ways[0][i] = 1


        for i in range(1,m+1):
            for j in range(1,n+1):
                ways[i][j] = ways[i-1][j] + ways[i][j-1]


        return ways[m-1][n-1]

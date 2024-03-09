"""
980. Unique Paths III
Solved
Hard
Topics
Companies
You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

Example 1:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:


Input: grid = [[0,1],[2,0]]
Output: 0
Explanation: There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
1 <= m * n <= 20
-1 <= grid[i][j] <= 2
There is exactly one starting cell and one ending cell.
"""

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        self.res = 0
        visited = set()
        
        def dfs(r, c):
            if grid[r][c] == 2 and len(visited) == (R*C-1-countit):
                self.res += 1
                return 
            visited.add((r,c))
            for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)]:
                r_ = r+dr
                c_ = c+dc
                if (
                    (r_,c_) not in visited 
                    and r_ in range(R) 
                    and c_ in range(C)
                    and grid[r_][c_] in [0, 2]):
                    dfs(r_, c_) 
            visited.remove((r,c))

        countit = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == -1:
                    countit += 1
                elif grid[r][c] == 1:
                    start = (r,c)
                
        dfs(start[0], start[1])

        return self.res

        

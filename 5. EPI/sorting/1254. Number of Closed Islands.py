"""
1254. Number of Closed Islands
Solved
Medium

Topics

Companies

Hint
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

 

Example 1:



Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
"""

class Solution:
    def __init__(self):
        self.flag = False
    def closedIsland(self, grid: List[List[int]]) -> int:

        R, C = len(grid), len(grid[0])
        visited = set()

        def dfs(r,c):
            if (
                r not in range(R) or
                c not in range(C) or
                (r,c) in visited or
                grid[r][c] == 1
            ):
                return 
            
            visited.add((r,c))

            if (r == R-1) or (c == C-1) or (r == 0) or (c == 0):
                self.flag = True

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c-1)
            dfs(r, c+1)

            return

        count = 0
        for r in range(R):
            for c in range(C):

                if grid[r][c] == 0 and (r, c) not in visited:
                    dfs(r,c)
                    if not self.flag:
                        count += 1
                    self.flag = False

        return count


        

        

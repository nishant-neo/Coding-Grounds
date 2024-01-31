"""
994. Rotting Oranges
Solved
Medium
Topics
Companies
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        R, C = len(grid), len(grid[0])
        rotten = []
        fresh = []

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    rotten.append((r,c))
                elif grid[r][c] == 1:
                    fresh.append((r,c))
        fresh = set(fresh)
        if len(fresh) == 0:
            return 0

        visited = set()
        count_hops = 0
        while(len(rotten)>0):
            to_iter = len(rotten)
            count_hops += 1
            for _ in range(to_iter):
                
                r,c = rotten.pop(0)
                visited.add((r,c))
                if (r,c) in fresh:
                    fresh.remove((r,c))
                for dx,dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    
                    r_ = r+dx
                    c_ = c+dy
                    if (
                        r_ in range(R) and 
                        c_ in range(C) and 
                        (r_,c_) not in visited and
                        grid[r_][c_] == 1):

                        rotten.append((r_,c_))
                        if (r,c) in fresh:
                            fresh.remove((r,c))

            if len(fresh) == 0:
                return count_hops-1
            # print(fresh, rotten)

        return -1





            
            
        

                




        # visited = set()
        # rotten_visited = set()
        # rotten = set()

        # def dfs(r, c):
        #     if (
        #         r in range(R) and
        #         c in range(C) and
        #         (r,c) not in visited and
        #         grid[r][c] == 1):

        #         visited.add((r,c))
        #         rotten_visited.add((r,c))

        #         return 1 + max(dfs(r+1, c), dfs(r-1, c), dfs(r, c+1), dfs(r, c-1))

        #         visited.remove((r,c))

        #     else:
        #         return 0


        # for r in range(R):
        #     for c in range(C):
        #         if grid[r][c] == 2:
        #             rotten.add((r,c))
        #             dfs(r, c)
                


        

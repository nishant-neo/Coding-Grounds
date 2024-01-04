"""
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

 

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

Constraints:

n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.
"""

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        # visited = set()
        # # print(R,C)
        
        # def dfs(r,c, count):
        #     # print("before ", r, c)
        #     if ( (r < 0 or r >= R) or
        #          (c < 0 or c >= C) or
        #          (r,c) in visited or
        #          grid[r][c] == 0
        #     ):
        #         return
        #     # print((r,c))
        #     res.append((r,c))
        #     grid[r][c] = 2

        #     visited.add((r,c))
        #     if c+1 < C and grid[r][c+1] > 0:
        #         dfs(r,c+1, count)
        #     if c-1 >= 0 and grid[r][c-1] > 0:
        #         dfs(r,c-1, count)
        #     if r+1 < R and grid[r+1][c] > 0:
        #         dfs(r+1,c, count)
        #     if r-1 >= 0 and grid[r-1][c] > 0:
        #         dfs(r-1,c, count)

        #     visited.remove((r,c))

        #     return

        # res = []
        # count = 0
        # flag = False
        # for r in range(R):
        #     for c in range(C):
        #         if grid[r][c] == 1 and (r,c) not in res:
        #             # print(f"start ({r},{c})")
        #             dfs(r,c, count)
        #             count+=1
        #             flag = True
        #             break
        #     if flag:
        #         break
        # # print(res)
        m, n = len(grid), len(grid[0])
        i, j = next((i, j) for i in range(m) for j in range(n) if grid[i][j])
        
        # dfs 
        stack = [(i, j)]
        seen = set(stack)
        while stack: 
            i, j = stack.pop()
            seen.add((i, j)) # mark as visited 
            grid[i][j] = 2
            for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] and (ii, jj) not in seen: 
                    stack.append((ii, jj))
                    
                    seen.add((ii, jj))

        print(seen)

        res = [ ((a,b),0) for a,b in seen]
        print(res)

       
        min_dis = R+C
        dq=deque(res)
        visited = set()
        while len(dq)>0:
            
            (r,c), count = dq.popleft()
            # print((r,c), count)
            if grid[r][c] == 1:
                return count-1
            if (r,c) in visited:
                continue
            visited.add((r,c))
            if c+1 < C :
                dq.append(((r,c+1),count+1))
            if c-1 >= 0 : 
                dq.append(((r,c-1),count+1))
            if r+1 < R  : 
                dq.append(((r+1,c),count+1))
            if r-1 >= 0 : 
                dq.append(((r-1,c),count+1))

            
            
        
        
        return 1


        

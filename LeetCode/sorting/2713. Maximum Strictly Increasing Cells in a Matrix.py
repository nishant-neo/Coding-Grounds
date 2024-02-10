"""
2713. Maximum Strictly Increasing Cells in a Matrix
Solved
Hard
Topics
Companies
Hint
Given a 1-indexed m x n integer matrix mat, you can select any cell in the matrix as your starting cell.

From the starting cell, you can move to any other cell in the same row or column, but only if the value of the destination cell is strictly greater than the value of the current cell. You can repeat this process as many times as possible, moving from cell to cell until you can no longer make any moves.

Your task is to find the maximum number of cells that you can visit in the matrix by starting from some cell.

Return an integer denoting the maximum number of cells that can be visited.

 

Example 1:



Input: mat = [[3,1],[3,4]]
Output: 2
Explanation: The image shows how we can visit 2 cells starting from row 1, column 2. It can be shown that we cannot visit more than 2 cells no matter where we start from, so the answer is 2. 
Example 2:



Input: mat = [[1,1],[1,1]]
Output: 1
Explanation: Since the cells must be strictly increasing, we can only visit one cell in this example. 
Example 3:



Input: mat = [[3,1,6],[-9,5,7]]
Output: 4
Explanation: The image above shows how we can visit 4 cells starting from row 2, column 1. It can be shown that we cannot visit more than 4 cells no matter where we start from, so the answer is 4. 
 

Constraints:

m == mat.length 
n == mat[i].length 
1 <= m, n <= 105
1 <= m * n <= 105
-105 <= mat[i][j] <= 105

"""

from sortedcontainers import SortedSet
class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        # Let m and n be the number of rows and columns of the matrix. 
        # Create 2 arrays r and c whose lengths are m and n. 
        # Initialize them to all 0s. 
        # They are the maximum path length of each row or column.
        nums = []
        m, n = len(mat), len(mat[0])
        r, c = [0]*m, [0]*n

        # Sort all the values in the matrix in non increasing order, 
        # for each value v, save all the positions (x, y) of that value 
        # in a list (reverse indexed).
        vmap = defaultdict(list)
        s = SortedSet()
        for i in range(m):
            for j in range(n):
                vmap[mat[i][j]].append([i, j])
                s.add(mat[i][j])

        # Loop all the values from largest to smallest, 
        # for each v, all the occurrence positions (x, y), 
        # save temp[x][y] = max(r[x], c[y]) + 1, this is the longest path 
        # starting from that value.
        temp = [[0]*n for _ in range(m)]
        for x in s:
            for v in vmap.get(x):
                temp[v[0]][v[1]] = max(r[v[0]], c[v[1]]) + 1

            # Update r[x] = max(r[x], temp[x][y]) and c[y] = max(c[y], 
            # temp[x][y]) for all the above (x, y)s. This is to update the longest 
            # path for each row and column. Also note this step should be done 
            # after step 3 is fully complete.
            for v in vmap.get(x):
                r[v[0]] = max(r[v[0]], temp[v[0]][v[1]])
                c[v[1]] = max(c[v[1]], temp[v[0]][v[1]])
        return max(max(r), max(c))
    

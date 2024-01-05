"""
74. Search a 2D Matrix
Solved
Medium

Topics

Companies
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])

        index_col = []
        for r in range(R):
            index_col.append(matrix[r][0])

        idx = bisect.bisect_right(index_col, target)-1

        if idx == -1:
            return False

        idx2 = bisect.bisect_right(matrix[idx], target)

        if matrix[idx][idx2-1] == target:
            return True


        return False
        

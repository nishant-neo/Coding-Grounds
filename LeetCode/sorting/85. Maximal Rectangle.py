"""
85. Maximal Rectangle
Solved
Hard
Topics
Companies
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = [["0"]]
Output: 0
Example 3:

Input: matrix = [["1"]]
Output: 1
 

Constraints:

rows == matrix.length
cols == matrix[i].length
1 <= row, cols <= 200
matrix[i][j] is '0' or '1'.
"""

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        R, C = len(matrix), len(matrix[0])
        matrix_sum_col = [[0 for i in range(C)] for j in range(R)]

        for j in range(C):
            matrix_sum_col[0][j] = 1 if matrix[0][j] == '1' else 0
        
        for j in range(C):
            for i in range(1, R):
                if matrix[i][j] == '1':
                    matrix_sum_col[i][j] = 1+matrix_sum_col[i-1][j]
                else:
                    matrix_sum_col[i][j] = 0

        print(matrix_sum_col)

        def maximum_rectangle_in_histogram(hist):
            n = len(hist)
            stack = []
            
            max_area = hist[0]
            for idx, num in enumerate(hist):
                cur_idx = idx
                while len(stack)>0 and stack[-1][0] > num:
                    popped = stack.pop()
                    max_area = max(max_area, (idx-popped[1])*popped[0])
                    cur_idx = popped[1]
                stack.append((num, cur_idx))

            for height, idx in stack:
                max_area = max(max_area , (n-idx)*height)

            return max_area



        max_rect = 0
        for row in matrix_sum_col:
            print(row)
            area = maximum_rectangle_in_histogram(row)
            max_rect = max(max_rect, area)

        
        return max_rect
        
